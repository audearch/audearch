import configparser
from pymongo import MongoClient


class Database(object):
    __client = None
    __db = None
    __collection = None

    def __init__(self, collectionName):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__dbname = config['DATABASE']['db']
        self.__client = MongoClient()
        self.__db = self.__client[self.__dbname]
        self.__collection = self.__db.get_collection(collectionName)

    def insert(self, id, hsh, starttime):
        post = {
            'music_id': id,
            'music_hash': hsh,
            'music_starttime': starttime
        }

        return self.__collection.insert_one(post)

    def find(self, projection=None, filter=None, sort=None):
        return self.__collection.find(projection=projection, filter=filter, sort=sort)
