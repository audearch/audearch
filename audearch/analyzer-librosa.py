from typing import List

import librosa
import numpy as np
from scipy import ndimage as ndi

import analyzer


def librosa_analyzer(path: str, size: int) -> List:
    y = librosa.load(path)
    Zxx1 = librosa.stft(y[0])
    sgram = np.abs(Zxx1)
    sgrammax = ndi.maximum_filter(sgram, size=size, mode="constant")
    maxima = (sgram == sgrammax) & (sgram > 0.2)
    peak_freq, peak_time = np.where(maxima)

    ans = analyzer.peak_to_landmark(peak_freq, peak_time)

    return ans
