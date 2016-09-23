from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
def main():
    connection=MongoClient('localhost',27017)
    db=connection.views
    collection=db.users


    user =raw_input("Enter Username:")
    user=user.encode()
    password=raw_input('Enter Password:')
    password=password.encode()
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    try:
        collection.insert({'Username':user,'Password':pass_hash})
        print 'User Successfully Created'
        print str(collection.find())
    except DuplicateKeyError:
        print 'user already present'
main()


