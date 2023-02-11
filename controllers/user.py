from models.user import User
from utils.error import CustomICCError

class UserController():
    def create_user(user_obj: dict):
        user = User.parse_obj(user_obj)
        user.update()
        return user.dict()

    def update_user():
        pass

    def get_user(user_id):
        user = User.find_one(user_id)
        if not user:
            return CustomICCError.USER_NOT_FOUND
        return user.dict()
    

    def find_user(params: dict):
        user = User.find_one(params)
        if not user:
            return CustomICCError.USER_NOT_FOUND
        return user.dict()
    
    def find_users(params: dict):
        users = User.find_many(params)
        if not len(users):
            return CustomICCError.USERS_NOT_FOUND
        return [user.dict() for user in users]
    
        
        

