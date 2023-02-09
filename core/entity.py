from time import time
from bson import ObjectId
from dataclasses import dataclass, field
from core.db_manager import DBManager

@dataclass
class Entity:
    _id: ObjectId = field(default_factory=ObjectId)
    created_at: float = field(default_factory=time)
    updated_at: float = field(default_factory=time)
    deleted: bool = False

    @classmethod
    def _db(cls, secondary=True):
        db_manager = DBManager.get_instance()
        return db_manager.get_collection(cls)

    def update(self, keys=[]):
        self.u = time()
        ndict = self.__dict__
        if (len(keys) == 0):
            self._db(False).update_one({"_id": self._id}, {"$set": ndict},  upsert=True)
        else:
            d2 = {x:ndict.get(x) for x  in keys if x in ndict}
            if (len(d2) >0):
                self._db(False).update_one({"_id": self._id}, {"$set": d2},  upsert=True)