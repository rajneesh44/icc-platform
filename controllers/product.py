from models.product import Product
from utils.error import CustomICCError

class ProductController:
    def add_product(self, data: dict):
        product = Product.parse_obj(data)
        product.update()
        return product.dict()
    
    def list_products(self):
        products = Product.find_many({})
        return [product.dict() for product in products]
    
    def get_product(self, product_id: str):
        product = Product.find_one({"uuid": product_id})
        if not product:
            return CustomICCError.PRODUCT_NOT_FOUND
        return product.dict()
    
        

