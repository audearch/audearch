import configparser
from abc import ABCMeta, abstractmethod

from pymongo import MongoClient


class DatabaseFactory(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def connect_database(cls):
        pass

    def create(self):
        d = self.connect_database()

        return d


class Database(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def insert_music(cls):
        pass

    @classmethod
    @abstractmethod
    def insert_music_metadata(cls):
        pass

    @classmethod
    @abstractmethod
    def find_music(cls):
        pass


class Mongodb(Database):
    def __init__(self, database, conf):
        self.__db = database
        self.__config = conf

    def insert_music(self, music_id, hsh, starttime):
        self.__collection = self.__db.get_collection(self.__config['MongoDB']['music_collectionname'])

        post = {
            'music_id': music_id,
            'music_hash': hsh,
            'music_starttime': starttime
        }

        self.__collection.insert_one(post)

    def insert_music_metadata(self, music_id, title, duration):
        self.__collection = self.__db.get_collection(self.__config['MongoDB']['music_metadata_collectionname'])

        music_metadata = {
            'music_id': music_id,
            'music_title': title,
            'music_duration': duration
        }

        self.__collection.insert_one(music_metadata)

    def find_music(self, projection=None, filter=None, sort=None):
        return self.__collection.find(projection=projection, filter=filter, sort=sort)


class MongodbFactory(DatabaseFactory):
    def __init__(self):
        self.__client = None
        self.__db = None

    def connect_database(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('audearch-config.ini')

        self.__client = MongoClient(host=self.__config['MongoDB']['host'], port=int(self.__config['MongoDB']['port']))
        self.__db = self.__client[self.__config['MongoDB']['dbname']]

        self.__database = Mongodb(self.__db, self.__config)

        return self.__database
