import wave
import numpy as np
from scipy import signal

main_wave, main_wave_rate = open_wavfile()
array = transform_nparray(main_wave)

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

    wave_file = wave.open(wave_path, rb)
    rate = wave_file.getframerate()

    return wave_file,rate

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
    """

    narray = orignal_wave.readframes(orignal_wave.getnframes())
    narray = np.frombuffer(narray, dtype="int16")

    return narray
