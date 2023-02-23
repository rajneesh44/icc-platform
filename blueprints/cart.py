from flask import Blueprint, request, session
from controllers.cart import CartController
from utils.response_utils import compose_response
from utils.error import CustomICCError

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")
cc = CartController()


@cart_blueprint.route("/add", methods=["POST"])
def add_to_cart():
    uid = session.get("uid")
    data = request.json
    product_id = data.get("product_id")
    size = data.get("size")
    if not uid or not product_id:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    return compose_response(cc.add_to_cart(uid, product_id, size))


@cart_blueprint.route("/info", methods=["GET"])
def get_cart_info():
    uid = session.get("uid")
    return compose_response(cc.get_cart_info(uid))