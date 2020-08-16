import configparser
from abc import ABCMeta, abstractmethod

from pymongo import MongoClient


class DatabaseFactory(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def connect_database(cls):
        pass

    @classmethod
    @abstractmethod
    def create_database(cls, db):
        pass

    def create(self):
        self.__db = self.connect_database()

        d = self.create_database(self.__db)
        return d


class Database(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def insert_music(cls):
        pass

    @classmethod
    @abstractmethod
    def find_music(cls):
        pass


class Mongodb(Database):
    __collection = None

    def __init__(self, db):
        self.__collection = db

    def insert_music(self, music_id, hsh, starttime):
        post = {
            'music_id': music_id,
            'music_hash': hsh,
            'music_starttime': starttime
        }

        return self.__collection.insert_one(post)

    def find_music(self, projection=None, filter=None, sort=None):
        return self.__collection.find(projection=projection, filter=filter, sort=sort)


class MongodbFactory(DatabaseFactory):
    def __init__(self):
        self.__client = None
        self.__db = None
        self.__collection = None

    def connect_database(self):
        config = configparser.ConfigParser()
        config.read('audearch-config.ini')

        self.__client = MongoClient(host=config['MongoDB']['host'], port=int(config['MongoDB']['port']))
        self.__db = self.__client[config['MongoDB']['dbname']]
        self.__collection = self.__db.get_collection(config['MongoDB']['collectionname'])

        return self.__collection

    def create_database(self, db):
        self.__database = Mongodb(db)
        return self.__database
