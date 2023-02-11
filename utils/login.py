import os
from flask import session
from functools import wraps
import time
from utils.response_utils import compose_response
from utils.error import CustomICCError


def login_user(data: dict):
    session["uid"] = data.get("uid", data.get("id"))
    session["t"] = time.time()
    session["logout"] = False
    session["user_type"] = data.get("user_type")
    session["expiry"] = int(time.time()) + int(os.getenv("COOKIE_EXPIRATION_TIME"))


# def logout_user(uid):
#     session["logout"] = True
#     if "uid" in session:
#         del session ["uid"]
#     session.modified = True


def login_required(func):
    @wraps(func)
    def decorator(*agrs, **kwargs):
        uid = session.get("uid", None)
        logout = session.get("logout", None)
        expiry = int(session.get("expiry", 0))
        user_type = int(session.get("user_type", 0))
        if (
            uid is None 
            or logout
            or expiry < time.time()
            or user_type != 0
        ):
            return compose_response(CustomICCError.UNAUTHORIZED)
        session["t"] = time.time()
        return func()
    return decorator


def admin_required(func):
    @wraps(func)
    def decorator(*agrs, **kwargs):
        uid = session.get("uid", None)
        logout = session.get("logout", None)
        expiry = int(session.get("expiry", 0))
        user_type = int(session.get("user_type", 0))
        if (
            uid is None 
            or logout
            or expiry < time.time()
            or user_type !=1
        ):
            return compose_response(CustomICCError.UNAUTHORIZED)
        session["t"] = time.time()
        return func()
    return decorator