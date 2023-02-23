from flask import Blueprint, session, request
from controllers.address import AddressController
from utils.response_utils import compose_response
from utils.login import login_required


address_blueprint = Blueprint("address", __name__, url_prefix="/address")
ac = AddressController()

@address_blueprint.route("/add", methods=["POST"])
@login_required
def add_address():
    uid = session.get("uid")
    data = request.json
    return compose_response(ac.add_address(uid, data))


@address_blueprint.route("/", methods=["GET"])
@login_required
def list_address():
    uid = session.get("uid")
    return compose_response(ac.list_addresses(uid))


@address_blueprint.route("/update", methods=["POST"])
@login_required
def update_address():
    uid = session.get("uid")
    data = request.json
    return compose_response(ac.update_address(uid, data))


@address_blueprint.route("/delete", methods=["POST"])
@login_required
def delete_address():
    address_id = request.json.get("address_id")
    return compose_response(ac.delete_address(address_id))