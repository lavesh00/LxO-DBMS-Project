from pymongo import MongoClient
from bson import ObjectId
from get_connection import get_mongo_connection

class NoSQLAgent:
    def __init__(self):
        self.collection = get_mongo_connection()

    def insert_data(self, data):
        """Insert unstructured data into MongoDB"""
        try:
            self.collection.insert_one(data)
            return {"message": "Data inserted into MongoDB successfully!"}
        except Exception as e:
            return {"error": str(e)}

    def fetch_data(self):
        """Fetch data from MongoDB"""
        try:
            data = list(self.collection.find())
            # Convert ObjectId fields to strings for JSON serialization
            for document in data:
                if "_id" in document:
                    document["_id"] = str(document["_id"])
            return data
        except Exception as e:
            return {"error": str(e)}
