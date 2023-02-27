from flask  import Blueprint, session, request
from controllers.user import UserController
from utils.login import login_required, admin_required
from utils.response_utils import compose_response


user_blueprint = Blueprint("user", __name__, url_prefix="/user")
uc = UserController()


@user_blueprint.route("/", methods=["GET"])
@login_required
def get_user():
    uid = session.get("uid")
    user = uc.get_user(uid)
    return compose_response(user)


@user_blueprint.route("/admin", methods=["GET"])
@admin_required
def get_admin():
    uid = session.get("uid")
    user = uc.get_user(uid)
    return compose_response(user)


@user_blueprint.route("/update", methods=["POST"])
@login_required
def update_user():
    uid = session.get("uid")
    data = request.json
    data["user_id"] = uid
    user = uc.update_user(data)
    return compose_response(user)