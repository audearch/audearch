import configparser
from pymongo import MongoClient
from abc import ABCMeta, abstractmethod


class DatabaseFactory(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def connect_database(self):
        pass

    @classmethod
    @abstractmethod
    def create_database(self, db):
        pass

    def create(self):
        self.__db = self.connect_database()

        d = self.create_database(self.__db)
        return d


class Database(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def insert(self):
        pass

    @classmethod
    @abstractmethod
    def find(self):
        pass


class Mongodb(Database):
    __collection = None

    def __init__(self, db):
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

    def connect_database(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__client = MongoClient()
        self.__db = self.__client[config['MongoDB']['dbname']]
        self.__collection = self.__db.get_collection(config['MongoDB']['collectionname'])

        return self.__collection

    def create_database(self, db):
        self.__database = Mongodb(db)
        return self.__database
