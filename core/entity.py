from time import time
from typing import Any
from core.db_manager import DBManager
from bson import ObjectId
from dataclasses import dataclass, is_dataclass, field


def from_dict_utils(cls, ndict):
    d2 = {}
    for key in cls.__dataclass_fields__.keys():
        if key not in ndict:
            continue
        value = cls.__dataclass_fields__[key].type
        if ndict.get(key) is not None and value in [str,float,int]:
            d2[key] = value(ndict.get(key))
        elif value == bool:
            if ndict.get(key) in ["true", "True", True]:
                d2[key] = True
            elif ndict.get(key) in ["false", "False", False]:
                d2[key] = False
        elif ndict.get(key) is not None and is_dataclass(value):
            d2[key] = from_dict_utils(value, ndict.get(key))
        else:
            d2[key] = ndict.get(key)
    if "_id" in ndict and "_id" not in d2:
        d2["_id"] = ndict.get("_id")

    return d2

@dataclass
class Entity():
    created_at: float = field(default_factory=time)
    updated_at: float = field(default_factory=time)
    deleted: bool = False
    _id: ObjectId = field(default_factory=ObjectId)


    @classmethod
    def from_dict(cls, ndict):
        if ndict is None:
            return None
        d2 = from_dict_utils(cls, ndict)
        return cls(**d2)
    
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
        return cls.from_dict(obj)
    
    @classmethod 
    def find_many(cls, params, keys=[], deleted=False, limit=0, sort=None):
        db = cls._db()

        if not isinstance(params, dict):
            olist = [ObjectId(_id) if ObjectId.is_valid(_id) else _id for _id in params ]
            params = {"_id":{"$in": olist}}
        if not deleted:
            params.update({"deleted":{"$ne":True}})

        cur = db.find(filter=params, projection=keys, limit=limit, sort=sort)

        return [cls.from_dict(obj) for obj in cur]

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
