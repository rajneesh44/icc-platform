from flask import session


def login_user(data):
    session["uid"] = str(data)
