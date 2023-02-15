from flask import Blueprint, request
from utils.response_utils import compose_response
from controllers.product import ProductController

product_blueprint = Blueprint("product", __name__, url_prefix="/products")
pc = ProductController()

@product_blueprint.route("/", methods=["GET"])
def list_products():
    return compose_response(pc.list_products())

@product_blueprint.route("/<uuid>", methods=["GET"])
def get_product(uuid: str):
    return compose_response(pc.get_product(uuid))

@product_blueprint.route("/add", methods=["POST"])
def add_product():
    data = request.json
    return compose_response(pc.add_product(data))

