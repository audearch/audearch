import pytest

import audearch.register as ar
import audearch.search as search


class TestSearch:

    @staticmethod
    def test_search(db_connection):
        COLLRCT_ID = 1
        imongodb = db_connection

        ar.register(1, 'tests/testmusic/1.wav', 3, imongodb)
        ar.register(2, 'tests/testmusic/2.wav', 3, imongodb)
        ar.register(3, 'tests/testmusic/3.wav', 3, imongodb)
        ar.register(4, 'tests/testmusic/4.wav', 3, imongodb)
        ar.register(5, 'tests/testmusic/5.wav', 3, imongodb)

        ansid = search.search('tests/testmusic/1.wav', 3, imongodb)

        assert COLLRCT_ID == ansid


if __name__ == '__main__':
    pytest.main()
