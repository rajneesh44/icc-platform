from flask import Blueprint, request, session
from bson import ObjectId
from models.user import User
from controllers.auth import AuthController


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
ac = AuthController()

@auth_blueprint.route("/google/callback", methods=["POST"])
def google_auth():
    data = request.json
    idToken = data.get("idToken")
    if not idToken:
        return "Error"
    return ac.google_auth_callback(idToken)
