from pymongo import MongoClient
from flask_pymongo import MongoClient
import pymongo
class Config:
    WTF_CSRF_ENABLED = True
    MONGO_DBNAME= 'UserData'
    DB_NAME = 'UserData'
    DB=MongoClient('')[DB_NAME]
    USER_COLLECTION=DB.users
    DEBUG=True