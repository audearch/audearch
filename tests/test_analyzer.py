import unittest
import os
import auderch.analyzer as analyzer
from numpy.testing import assert_array_equal
import numpy as np


class TestAnalyzer(unittest.TestCase):

    def test_open_wavefile(self):
        filepath = os.getcwd() + '/tests/test.wav'
        file, rate = analyzer.open_wavfile(filepath)

        exwavrate = 8000

        self.assertEqual(exwavrate, rate)

    def test_transform_nparray(self):
        wavfile, rate = analyzer.open_wavfile("tests/test.wav")
        narray, narray_frame = analyzer.transform_nparray(wavfile)
        a = 1  # 振幅
        fs = 8000  # サンプリング周波数
        f0 = 440  # 周波数
        sec = 5  # 秒

        swav = []

        for n in np.arange(fs * sec):
            # サイン波を生成
            s = a * np.sin(2.0 * np.pi * f0 * n / fs)
            swav.append(s)

        swav = [int(x * 32767.0) for x in swav]

        assert_array_equal(swav, narray)


if __name__ == "__main__":
    unittest.main()
