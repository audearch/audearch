import hashlib
import wave
from typing import Dict, List, Tuple

import librosa
import numpy as np
from scipy import ndimage as ndi
from scipy import signal
from tqdm import tqdm


def open_wavfile(wave_path: str) -> Tuple[wave.Wave_read, int]:
    """
    get wavefile

    Parameters
    ----------
    wave_path : string
        wavefile path

    Returns
    ----------
    wave_file : file
        wavefile(file-like object)
    """

    wave_file = wave.open(wave_path, 'rb')
    rate = wave_file.getframerate()

    return wave_file, rate


def transform_nparray(orignal_wave: wave.Wave_read) -> Tuple[np.ndarray, int]:
    """transform wave into ndarray

    Parameters
    ----------
    orignal_wave : file
        wave_read object

    Returns
    -------
    narray : ndarray
        1-d array
    narray_frame : int
        frame_length
    """

    narray_frame = orignal_wave.getnframes()
    narray = orignal_wave.readframes(narray_frame)
    narray = np.frombuffer(narray, dtype="int16")

    return narray, narray_frame

# TODO:write more description


def find_peak(s: np.ndarray, fs: int, size: int) -> Tuple[np.ndarray, np.ndarray]:
    Zxx1 = signal.stft(s, fs=fs)
    sgram = np.abs(Zxx1[2])
    sgrammax = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgrammax) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)
    return peak_freq, peak_time


def peak_to_landmark(peaks_freq: np.ndarray, peaks_time: np.ndarray, target_freq: int = 10, target_time: int = 10, target_dist: int = 10) -> List:

    landmarks = []

    bar = tqdm(total=len(peaks_freq))

    for anc_freq, anc_time in zip(peaks_freq, peaks_time):
        firsttime: int = anc_time + target_time
        endtime: int = firsttime + target_dist
        target: Dict[int, int] = dict(zip(peaks_time, peaks_freq))
        zone = {k: v for k, v in target.items() if int(k) >
                firsttime and int(k) < endtime}
        for ptime_target, pfreq_target in list(zone.items()):
            disttime = int(ptime_target) - anc_time

            hsh = hashlib.sha256((anc_time << 6) | ((pfreq_target+target_freq-anc_freq) << 8) | (disttime)).hexdigest()

            landmarks.append((hsh, anc_time))

        bar.update(1)

    return landmarks


def analyzer(path: str, size: int) -> List:
    main_wave = open_wavfile(path)
    array, frames = transform_nparray(main_wave[0])
    pf, pt = find_peak(array, frames, size)
    list_landmark = peak_to_landmark(pf, pt)

    return list_landmark


def librosa_analyzer(path: str, size: int) -> List:
    y = librosa.load(path)
    Zxx1 = librosa.stft(y[0])
    sgram = np.abs(Zxx1)
    sgrammax = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgrammax) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)

    ans = peak_to_landmark(peak_freq, peak_time)

    return ans
