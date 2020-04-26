import wave
import numpy as np
import functions as fn
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


def stft(onedarray, array_rate, array_frames):
    """short-time fourier transform

    Parameters
    ----------
    onedarray : 1-d nparray
        [description]
    array_rate : string
        [description]
    array_frames : string
        [description]

    Returns
    -------
    2-d nparray
        [description]
    """

    # monauralize 1-darray
    x = fn.monauralize(onedarray)

    # define song parameter
    nfft = 1024
    overlap = nfft / 2
    sampling_rate = array_rate
    frame_length = array_frames
    time_song = float(frame_length) / sampling_rate
    time_unit = 1 / float(sampling_rate)

    # define fft-frame parameter
    start = (nfft / 2) * time_unit
    stop = time_song
    step = (nfft - overlap) * time_unit
    time_ruler = np.arrange(start, stop, step)

    # define window function
    window = np.hamming(nfft)

    spec = np.zeros([len(time_ruler), 1 + overlap])
    pos = 0

    for fft_index in range(len(time_ruler)):
        frame = x[pos:pos+nfft]

        if len(frame) == nfft:
            # multiply window function
            windowded = window * frame
            # get fft result
            fft_result = np.fft.rfft(windowded)

            for i in range(len(spec[fft_index])):
                spec[fft_index][-i-1] = fft_result[i]

            pos += (nfft - overlap)

    return spec


def find_peak(twoarray, size):
    sgram = np.abs(twoarray)
    sgram_max = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgram_max) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)
    return peak_freq, peak_time


main_wave, main_wave_rate = open_wavfile()
array, frames = transform_nparray(main_wave)
spec = stft(array, main_wave_rate, frames)
