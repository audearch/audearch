import wave
import numpy as np
from scipy import ndimage as ndi


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


def STFT(s, nframes, noverlap):
    """
    short time fourier transform

    Parameters
    ----------
    s : 1D nparray
        audio signal
    nframes : int
        the number of frames

    Returns
    -------
    np.complex128
        numpy complex number(both real-part and imaginaly-part is float64)
    """
    overlap = nframes//2
    nlines = s.shape[0]
    win = np.hanning(nframes)
    Mf = nframes//2 + 1
    Nf = int(np.ceil((nlines-overlap)/(nframes-overlap)))-1

    S = np.empty([Mf, Nf], dtype=np.complex128)

    for n in range(Nf):
        S[:, n] = np.fft.rfft(
            s[(nframes-overlap)*n:(nframes-overlap)*n+nframes] * win,
            n=nframes,
            axis=0)

    return S


def find_peak(twoarray, size):
    sgram = np.abs(twoarray)
    sgram_max = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgram_max) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)
    return peak_freq, peak_time


"""
main_wave, main_wave_rate = open_wavfile()
array, frames = transform_nparray(main_wave)
spec = stft(array, main_wave_rate, frames)
"""
