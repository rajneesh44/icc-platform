from models.product import Product
from utils.error import CustomICCError
from copy import deepcopy


class ProductController:
    def add_product(self, data: list):
        products = []
        for pd in data:
            product = Product.from_dict(pd)
            product.update()
            products.append(product)
        return [product.__dict__ for product in products]
    
    def list_products(self):
        products = Product.find_many({})
        return [product.__dict__ for product in products]
    
    def get_product(self, product_id: str) -> Product:
        product = Product.find_one({"uuid": product_id})
        if not product:
            return CustomICCError.PRODUCT_NOT_FOUND
        return product.__dict__
    
    def _get_product(self, product_id: str) -> Product:
        product = Product.find_one({"uuid": product_id})
        if not product:
            return CustomICCError.PRODUCT_NOT_FOUND
        return product


    def add_product_to_cart(self, product: Product, user_id: str, size=None):
        product_to_add = deepcopy(product)
        product_to_add.parent = product.uuid
        product_to_add.is_sku = False
        product_to_add.user_id = user_id
        product_to_add.quantity = 1
        if len(product.sizes):
            product_to_add.sizes = [size] if size else [product.sizes[(len(product.sizes)//2) - 1]]
        return product_to_add