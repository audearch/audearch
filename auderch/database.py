import configparser
from pymongo import MongoClient
from abc import ABCMeta, abstractmethod


class DatabaseFactory(metaclass=ABCMeta):

    @abstractmethod
    def __connect_database(self):
        pass

    @abstractmethod
    def __create_database(self):
        pass

    def create(self):
        self.__db = self.__connect_database()

        d = self.__create_database(self.__db)
        return d


class Database(metaclass=ABCMeta):

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def find(self):
        pass


class Mongodb(Database):
    __collection = None

    def ___init__(self, db):
        self.__collection = db

    def insert(self, id, hsh, starttime):
        post = {
            'music_id': id,
            'music_hash': hsh,
            'music_starttime': starttime
        }

        return self.__collection.insert_one(post)

    def find(self, projection=None, filter=None, sort=None):
        return self.__collection.find(projection=projection, filter=filter, sort=sort)


class MongodbFactory(DatabaseFactory):

    def __connect_database(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__client = MongoClient()
        self.__db = self.__client[config['MongoDB']['dbname']]
        self.__collection = self.__db.get_collection(config['MongoDB']['collectionname'])

    def __create_database(self, db):
        return Mongodb(db)
