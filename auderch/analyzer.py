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


"""
main_wave, main_wave_rate = open_wavfile()
array, frames = transform_nparray(main_wave)
pf, pt = find_peak(array, frames, 5)
"""
