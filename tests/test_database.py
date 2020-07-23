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

        assert result['music_hash'] == "6ee2e0a7cfbd562f1436ca43a73ba2afea0367244eaa3fa5cc71b826d42ea702"


if __name__ == '__main__':
    pytest.main()
