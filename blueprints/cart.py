from flask import Blueprint, request, session
from controllers.cart import CartController
from utils.response_utils import compose_response
from utils.error import CustomICCError
from utils.login import login_required

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")
cc = CartController()


@cart_blueprint.route("/add", methods=["POST"])
@login_required
def add_to_cart():
    uid = session.get("uid")
    data = request.json
    product_id = data.get("product_id")
    size = data.get("size")
    if not uid or not product_id or not size:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    return compose_response(cc.add_to_cart(uid, product_id, size))


@cart_blueprint.route("/remove", methods=["POST"])
@login_required
def remove_item_from_cart():
    uid = session.get("uid")
    data = request.json
    product_id = data.get("product_id")
    size = data.get("size")
    if not uid or not product_id or not size:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    return compose_response(cc.remove_from_cart(uid, product_id, size))


@cart_blueprint.route("/info", methods=["GET"])
@login_required
def get_cart_info():
    uid = session.get("uid")
    return compose_response(cc.get_cart_info(uid))