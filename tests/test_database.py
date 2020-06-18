import pytest
import auderch.database as ad
import auderch.analyzer as aa


class TestDatabase(object):

    def test_database(self):
        mongodb = ad.MongodbFactory()
        imongodb = mongodb.create()

        list_landmark = aa.analyzer("tests/test")

        for landmark in list_landmark:
            imongodb.insert(1, int(landmark[0]), int(landmark[1]))

        cur = imongodb.find(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        assert result['music_hash'] == int(57997)


if __name__ == '__main__':
    pytest.main()
