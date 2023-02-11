from flask import Blueprint, request, session
from models.user import User
from controllers.auth import AuthController
from utils.error import CustomICCError
from utils.response_utils import compose_response
from utils.login import login_required


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
ac = AuthController()

@auth_blueprint.route("/google/callback", methods=["POST"])
def google_auth():
    data = request.json
    idToken = data.get("idToken")
    if not idToken:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = ac.google_auth_callback(idToken)
    return compose_response(response)

@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return compose_response(True)
