import tornado.ioloop
import tornado.web
from datetime import datetime
from bson.json_util import dumps
import pymongo
from pymongo import MongoClient

MONGODB_DB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME ='listings'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]


class Listing(tornado.web.RequestHandler):

    def initialize(self, connection):
        self.conn = connection
        self.collection = db['listing_table']



    def get(self,connection):
        list = {
            "a":22
        }
        self.set_header('Content-Type', 'application/json')
        self.write(list)






def make_app():
    return tornado.web.Application([
        (r"/", Listing, dict(connection = client)),
        (r"/listing/([0-9]+)", Listing, dict(connection = client) ),

    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8887)
    tornado.ioloop.IOLoop.current().start()