__author__ = 'AL299758'

import json
from pymongo import MongoClient

# connect to the database
connection = MongoClient('localhost', 27017)

# access DB
db = connection.test

# handle the collection
names = db.names


for item in names.find():
    print(item)