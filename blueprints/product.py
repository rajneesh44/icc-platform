from flask import Blueprint, request
from utils.response_utils import compose_response
from controllers.product import ProductController
from utils.login import login_required, admin_required

product_blueprint = Blueprint("product", __name__, url_prefix="/products")
pc = ProductController()

@product_blueprint.route("/", methods=["GET"])
def list_products():
    return compose_response(pc.list_products())

@product_blueprint.route("/admin", methods=["GET"])
@admin_required
def admin_list_products():
    return compose_response(pc.list_products())

@product_blueprint.route("/<uuid>", methods=["GET"])
def get_product(uuid: str):
    return compose_response(pc.get_product(uuid))

@product_blueprint.route("/add", methods=["POST"])
@admin_required
def add_product():
    data = request.json.get("data", [])
    return compose_response(pc.add_product(data))

