from pymongo import MongoClient
import os
from dotenv import load_dotenv


def connection():
    load_dotenv()

    USERNAME = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DATABASE')
    COLLECTION = os.getenv('COLLECTION')

    CONNECTION_STRING = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.9ga3qrv.mongodb.net/'
    print(USERNAME)
    print(CONNECTION_STRING)
    mongoClient = MongoClient(CONNECTION_STRING, authSource = 'admin') 
    db = mongoClient[DATABASE]
    collection = db[COLLECTION]
    return collection