from models.user import User
from utils.error import CustomICCError

class UserController:
    def create_user(self,user_obj: dict):
        user = User.from_dict(user_obj)
        user.update()
        return user.__dict__

    def update_user(self, user_obj: dict):
        user = User.find_one(user_obj.get("user_id"))
        if not user:
            return CustomICCError.USER_NOT_FOUND
        user.update_document_from_dict(user_obj)
        return user.__dict__

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
    
    def check_referral_code(self, user_id, code):
        host = User.find_one({"referral_code": code})
        if not host:
            return CustomICCError.INVALID_REFERRAL_CODE
        
        user = User.find_one(user_id)
        if user and not user.referral_code_used:
            host = self._add_coins_to_user(str(host._id), 100)
            user = self._add_coins_to_user(str(user._id), 50)

            user.referral_code_used = True
            user.update()
        else:
            return CustomICCError.REFERRAL_CODE_ERROR
        return user.__dict__
    
    def _add_coins_to_user(self, user_id: str, coins: int):
        user = User.find_one(user_id)
        user.coins_earned += coins
        user.update()
        return user



    def _deduct_coins_from_user(self, user_id: str, coins: int):
        user = User.find_one(user_id)
        if (user.coins_earned - coins) >= 0:
            user.coins_earned -= coins
            user.update()
        return user.__dict__

    