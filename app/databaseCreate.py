from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
def main():
    connection=MongoClient('localhost',27017)
    db=connection.UserData
    collection=db.users


    user =raw_input("Enter Username:")
    password=raw_input('Enter Password:')
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    try:
        collection.insert({'id':user,'password':pass_hash})
        print 'User Successfully Created'
    except DuplicateKeyError:
        print 'user already present'
main()


