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
    data: dict = request.json
    idToken = data.get("idToken")
    if not idToken:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = ac.google_auth_callback(idToken)
    return compose_response(response)


@auth_blueprint.route("/send/otp", methods=["POST"])
def send_otp():
    data: dict = request.json
    phone = data.get("phone")
    if not phone:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = ac.send_otp(phone)
    return compose_response(response)

@auth_blueprint.route("/verify/otp", methods=["POST"])
def verify_otp():
    data: dict = request.json
    phone = data.get("phone")
    otp = int(data.get("otp", 0))
    if not (phone and otp):
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = ac.verify_otp(phone, otp)
    return compose_response(response)


@auth_blueprint.route("/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if not (username and password):
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = ac.login_admin_with_password(username, password)
    return compose_response(response)




@auth_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    return compose_response(True)
