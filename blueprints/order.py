from flask import Blueprint, request, session
from controllers.order import OrderController
from utils.error import CustomICCError
from utils.response_utils import compose_response
from utils.login import login_required


order_blueprint = Blueprint("order", __name__, url_prefix="/order")
oc = OrderController()

@order_blueprint.route("/checkout", methods=["POST"])
@login_required
def create_order():
    uid = session.get("uid")
    data = request.json
    cart_id = data.get("cart_id")
    if not uid or not cart_id:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    
    return compose_response(oc.create_order(uid, cart_id))

@order_blueprint.route("/", methods=["GET"])
@login_required
def get_orders():
    uid = session.get("uid")
    return compose_response(oc.list_orders(uid))

