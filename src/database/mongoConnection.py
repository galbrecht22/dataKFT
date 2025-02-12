import pymongo.errors
from pymongo import MongoClient
from typing import List, Dict


class MongoDBController:

    class MongoDBConnection:

        def __init__(self, host='localhost', port=27017):
            self.host = host
            self.port = port
            self.connection = None

        def __enter__(self):
            try:
                print('Connecting to MongoDB...')
                self.connection = MongoClient(host=self.host, port=self.port)
            except pymongo.errors.ConnectionFailure as e:
                print(f'Could not connect to {self.host}:{self.port}. Error: {e}')
                raise e
            else:
                print(f'Connected to {self.host}:{self.port}.')
                return self.connection

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.connection.close()
            print('Connection closed.')

    def __init__(self, database_name: str = 'dataKFT'):
        self.connection = self.MongoDBConnection()
        self.database_name = database_name
        self.collection_name = None

    def build(self):
        with self.connection as client:
            db = client.get_database(self.database_name)
            for col in ['tender', 'purchaser', 'ship']:
                db[col].drop()
                print(f'Dropped collection {self.database_name}.{col}.')
                db.create_collection(col)
                print(f'Created collection {self.database_name}.{col}.')

    def store(self, collection_name: str, documents: List[Dict]):
        with self.connection as client:
            db = client.get_database(self.database_name)
            collection = db.get_collection(collection_name)
            res = collection.insert_many(documents)
        return res

    def load(self, collection_name: str) -> List[Dict]:
        with self.connection as client:
            db = client.get_database(self.database_name)
            collection = db.get_collection(collection_name)
            res = collection.find({}, {'_id': False})
            return list(res)
