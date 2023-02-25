from flask import Blueprint, request, session
from utils.login import login_required
from utils.error import CustomICCError
from utils.response_utils import compose_response
from controllers.user import UserController


utils_blueprint = Blueprint("utils", __name__)
uc = UserController()


@utils_blueprint.route("/referral", methods=["GET"])
@login_required
def get_referral_code():
    uid = session.get("uid")
    code = request.args.get("code")
    if not code:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    return compose_response(uc.check_referral_code(uid, code))