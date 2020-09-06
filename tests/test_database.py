import pytest
import audearch.database as ad
import audearch.analyzer as aa


class TestDatabase:

    @staticmethod
    def test_database_insert_music():
        mongodb = ad.MongodbFactory()
        imongodb = mongodb.create()

        list_landmark = aa.analyzer("tests/test.wav", 5)

        for landmark in list_landmark:
            imongodb.insert_music(1, landmark[0], int(landmark[1]))

        cur = imongodb.find_music(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        assert result['music_hash'] == "6ee2e0a7cfbd562f1436ca43a73ba2afea0367244eaa3fa5cc71b826d42ea702"

    @staticmethod
    def test_database_insert_music_metadata():
        mongodb = ad.MongodbFactory()
        imongodb = mongodb.create()

        MUSIC_ID = 1
        TITLE = "TESTMUSIC"
        DURATION = 30

        imongodb.insert_music_metadata(MUSIC_ID, TITLE, DURATION)

        cur = imongodb.find_music(filter={'music_id': int(1)})

        result = dict(cur[0])

        assert result['music_duration'] == DURATION


if __name__ == '__main__':
    pytest.main()
