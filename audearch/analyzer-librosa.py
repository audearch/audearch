import librosa
import analyzer
import numpy as np
from scipy import ndimage as ndi


def librosa_analyzer(path, size):
    y, sr = librosa.load(path)
    Zxx1 = librosa.stft(y)
    sgram = np.abs(Zxx1)
    sgrammax = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgrammax) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)

    ans = analyzer.peak_to_landmark(peak_freq, peak_time)

    return ans
