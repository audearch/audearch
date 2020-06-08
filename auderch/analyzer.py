import wave
import numpy as np
from scipy import ndimage as ndi
from scipy import signal


def open_wavfile(wave_path):
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


def transform_nparray(orignal_wave):
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


def find_peak(s, fs, size):
    f1, t1, Zxx1 = signal.stft(s, fs=fs)
    sgram = np.abs(Zxx1)
    sgrammax = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgrammax) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)
    return peak_freq, peak_time


def peak_to_landmark(peaks_freq, peaks_time, target_freq=10, target_time=10, target_dist=10):
    F1_BITS = 8
    DF_BITS = 6
    DT_BITS = 6

    B1_MASK = (1 << F1_BITS) - 1
    B1_SHIFT = DF_BITS + DT_BITS
    DF_MASK = (1 << DF_BITS) - 1
    DF_SHIFT = DT_BITS
    DT_MASK = (1 << DT_BITS) - 1

    landmarks = []

    for anc_freq, anc_time in zip(peaks_freq, peaks_time):
        firsttime = anc_time + target_time
        endtime = firsttime + target_dist
        target = dict(zip(peaks_time, peaks_freq))
        zone = {k: v for k, v in target.items() if int(k) >
                firsttime and int(k) < endtime}
        for ptime_target, pfreq_target in list(zone.items()):
            disttime = int(ptime_target) - anc_time

            hsh = (((anc_freq & B1_MASK) << B1_SHIFT) | (
                ((pfreq_target+target_freq-anc_freq) & DF_MASK) << DF_SHIFT) | (disttime & DT_MASK))
            landmarks.append((hsh, anc_time))

    return landmarks
