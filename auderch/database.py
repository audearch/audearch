import mysql.connector
from mysql.connector import errorcode
import configparser


class Databese:
    __user = None
    __password = None
    __dbname = None
    __connection = None
    __cursor = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.__user = config['DATABASE']['user']
        self.__password = config['DATABASE']['password']
        self.__dbname = config['DATABASE']['dbname']

    def open(self):
        cnx = mysql.connector.connect(
            user=self.__user, passwd=self.__password, db=self.__dbname)

        self.__connection = cnx
        self.__cursor = cnx.cursor()

    def close(self):
        self.__cursor.close()
        self.__connection.close()
