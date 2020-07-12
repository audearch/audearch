import pytest
import audearch.database as ad
import audearch.analyzer as aa


class TestDatabase(object):

    def test_database(self):
        mongodb = ad.MongodbFactory()
        imongodb = mongodb.create()

        list_landmark = aa.analyzer("tests/test.wav")

        for landmark in list_landmark:
            imongodb.insert(1, landmark[0], int(landmark[1]))

        cur = imongodb.find(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        assert result['music_hash'] == "a4bd89d0c3e16ec03c5436d0b9b8eb1a934beeac808447459e5ee2f9a23e97d7"


if __name__ == '__main__':
    pytest.main()
