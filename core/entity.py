from time import time
from bson import ObjectId
from core.db_manager import DBManager
from pydantic import BaseModel

class Entity(BaseModel):
    created_at: float = time()
    updated_at: float = time()
    deleted: bool = False
    _id: ObjectId = ObjectId()


    @classmethod
    def _db(cls):
        db_manager = DBManager.get_instance()
        return db_manager.get_collection(cls)
    
    
    @classmethod
    def find_one(cls, params, keys=[], deleted=False):
        db = cls._db()
        is_object = isinstance(params, dict)
        if not is_object and not ObjectId.is_valid(params):
            params = {"_id": params}
        elif not is_object:
            params = {"_id": ObjectId(params)}
        if not deleted:
            params.update({"deleted":{"$ne":True}})
        if len(keys) == 0:
            obj = db.find_one(params)
        else:
            obj = db.find_one(params, keys)
        return cls.parse_obj(obj)
    
    @classmethod 
    def find_many(cls, params, keys=[], deleted=False, limit=0, sort=None):
        db = cls._db()

        if not isinstance(params, dict):
            olist = [ObjectId(_id) if ObjectId.is_valid(_id) else _id for _id in params ]
            params = {"_id":{"$in": olist}}
        if not deleted:
            params.update({"deleted":{"$ne":True}})

        cur = db.find(filter=params, projection=keys, limit=limit, sort=sort)

        return [cls.parse_obj(obj) for obj in cur]

    def update(self, keys=[]):
        db = self._db()
        self.updated_at = time()
        ndict = self.__dict__
        if (len(keys) == 0):
            db.update_one({"_id": self._id}, {"$set": ndict},  upsert=True)
        else:
            d2 = {x:ndict.get(x) for x  in keys if x in ndict}
            if (len(d2) >0):
                db.update_one({"_id": self._id}, {"$set": d2},  upsert=True)

    def delete(self, delete_from_db = False):
        db = self._db()
        if (delete_from_db):
            db.delete_one({"_id": self._id})
        else:
            db.update_one({"_id": self._id},{"$set":{"deleted":True}}, upsert = False)
    
    @classmethod
    def count_documents(cls, params, ):
        return cls._db().count_documents(params)
    

# add update_many, insert_many, delete_many as well.