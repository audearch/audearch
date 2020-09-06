import audearch.register as ar
import pytest


class TestRegister:

    @staticmethod
    def test_register(db_connection):
        imongodb = db_connection

        ar.register(1, 'tests/test.wav', 5, imongodb)

        cur = imongodb.find_music(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        assert result['music_hash'] == "6ee2e0a7cfbd562f1436ca43a73ba2afea0367244eaa3fa5cc71b826d42ea702"


if __name__ == '__main__':
    pytest.main()
