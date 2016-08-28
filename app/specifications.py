from pymongo import MongoClient

DB_NAME = 'UserData'
DB=MongoClient()[DB_NAME]
USER_COLLECTION=DB.users
