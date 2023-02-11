import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

class DBManager:
    instance = None

    def __init__(self) -> None:
        database_config = MongoClient(os.getenv("MONGO_URL"))
        self.db = database_config.get_database(self.get_db_name())
        
    
    @staticmethod
    def get_instance():
        return DBManager.instance
    
    @staticmethod
    def initialize_instance():
        DBManager.instance = DBManager()

    def get_db_name(self):
        return DB_NAME

    def get_collection_name(self, cls):
        return cls.__name__

    def get_collection(self, cls):
        db_collection = self.get_collection_name(cls)
        return self.db.get_collection(db_collection)
    


