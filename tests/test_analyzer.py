import pytest
import os
import audearch.analyzer as analyzer
from numpy.testing import assert_array_equal
import numpy as np


class TestAnalyzer:

    @staticmethod
    def test_open_wavefile():
        filepath = os.getcwd() + '/tests/test.wav'
        rate = analyzer.open_wavfile(filepath)

        exwavrate = 8000

        assert exwavrate == rate[1]

    @staticmethod
    def test_transform_nparray():
        wavfile = analyzer.open_wavfile("tests/test.wav")
        narray = analyzer.transform_nparray(wavfile[0])
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

        assert_array_equal(swav, narray[0])

    @staticmethod
    def test_find_peak():
        wavfile = analyzer.open_wavfile("tests/test.wav")
        narray, narray_frame = analyzer.transform_nparray(wavfile[0])
        pf, pt = analyzer.find_peak(narray, narray_frame, 5)

        test1 = 14
        test2 = 1

        assert_array_equal(test1, pf[0])
        assert_array_equal(test2, pt[0])

    @staticmethod
    def test_peak_to_landmark():
        wavfile = analyzer.open_wavfile("tests/test.wav")
        narray, narray_frame = analyzer.transform_nparray(wavfile[0])
        pf, pt = analyzer.find_peak(narray, narray_frame, 5)
        list_landmark = analyzer.peak_to_landmark(pf, pt)

        test1 = ("2ccef5329a1a780d069f120acfa7f53fb487e4570d9964c9db1f5190a740f93e", 1)

        assert_array_equal(test1, list_landmark[0])

    @staticmethod
    def test_analyzer():
        list_landmark = analyzer.analyzer("tests/test.wav", 5)

        test1 = ("2ccef5329a1a780d069f120acfa7f53fb487e4570d9964c9db1f5190a740f93e", 1)

        assert_array_equal(test1, list_landmark[0])


if __name__ == "__main__":
    pytest.main()
