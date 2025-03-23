import requests
import pymongo
import os

# TBD: change data source to timeseries data and simulate streaming

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
DB_NAME = "store"
COLLECTION_NAME = "products"
API_URL = "https://fakestoreapi.com/products"

def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def store_in_mongodb(data):
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    collection.insert_many(data)
    print(f"Inserted {len(data)} records into MongoDB.")

if __name__ == "__main__":
    data = fetch_data()
    store_in_mongodb(data)
