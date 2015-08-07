__author__ = 'AL299758'

import bottle
import pymongo


@bottle.route('/')
def index():
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    names = db.names

    item = names.find_one()
    return 'Hello <b>{0}</b>'.format(item['name'])

bottle.run(host='localhost', port=8000)