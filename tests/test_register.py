import audearch.register as ar
import pytest


class TestRegister(object):

    def test_register_one(self, db_connection):
        imongodb = db_connection

        ar.register_directory('/tests', imongodb)

        cur = imongodb.find(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        assert result['music_hash'] == int(57997)


if __name__ == '__main__':
    pytest.main()
