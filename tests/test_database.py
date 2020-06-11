import unittest
import auderch.database as ad
import auderch.analyzer as aa
import pymongo
from bson.json_util import dumps, loads


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.test_auderch
        self.collection = self.db['test-hashtable']

    def test_database(self):
        mongodb = ad.MongodbFactory()
        imongodb = mongodb.create()

        main_wave, main_wave_rate = aa.open_wavfile("C://Users/conta/desktop/dev/auderch/tests/test.wav")
        array, frames = aa.transform_nparray(main_wave)
        pf, pt = aa.find_peak(array, frames, 5)
        list_landmark = aa.peak_to_landmark(pf, pt)

        for landmark in list_landmark:
            imongodb.insert(1, int(landmark[0]), int(landmark[1]))

        cur = imongodb.find(filter={'music_starttime': int(12)})

        result = dict(cur[0])

        self.assertEqual(result['music_hash'], int(57997))


if __name__ == '__main__':
    unittest.main()
