from models.user import User
from utils.error import CustomICCError

class UserController:
    def create_user(self,user_obj: dict):
        user = User.from_dict(user_obj)
        user.update()
        return user.__dict__

    def update_user():
        pass

    def get_user(self, user_id):
        user = User.find_one(user_id)
        if not user:
            return CustomICCError.USER_NOT_FOUND
        return user.__dict__
    

    def find_user(self, params: dict):
        user = User.find_one(params)
        if not user:
            return CustomICCError.USER_NOT_FOUND
        return user.__dict__
    
    def find_users(self, params: dict):
        users = User.find_many(params)
        if not len(users):
            return CustomICCError.USERS_NOT_FOUND
        return [user.__dict__ for user in users]
    
        
        

