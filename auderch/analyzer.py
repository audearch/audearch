import wave

def open_wavfile(wave_resource):
    """
    get wavefile

    Parameters
    ----------
    wave_resource : string
        wavefile path
    
    Returns
    ----------
    wave_file : file
        wavefile(file-like object)
    """

    wave_file = wave.open(wave_resource)

    return wave_file
