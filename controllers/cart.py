from controllers.product import ProductController
from models.cart import Cart
from utils.error import CustomICCError
from dataclasses import asdict

pc = ProductController()

class CartController:
    def add_to_cart(self, user_id: str, product_id: str, size: str = None):
        sku_product = pc._get_product(product_id)
        if not sku_product or isinstance(sku_product, CustomICCError):
            return CustomICCError.PRODUCT_NOT_FOUND
        
        cart = Cart.find_one({"user_id": user_id})
        product_to_add = pc.add_product_to_cart(sku_product, user_id, size)
        
        if not cart:
            cart = Cart.from_dict({
                "products": [product_to_add],
                "user_id": user_id
            })
        else:
            product_found_in_cart = False
            for cart_product in cart.products:
                if cart_product.get("parent") == sku_product.uuid and [size] == cart_product.get("sizes"):
                    cart_product.update({"quantity": cart_product.get("quantity", 0)+1})
                    product_found_in_cart = True
                    break
    
            if not product_found_in_cart:
                cart.products.append(product_to_add)
        cart.update()
        return asdict(cart)

    def remove_from_cart(self, user_id: str, product_id: str):
        pass

    def get_cart_info(self, user_id: str):
        cart = Cart.find_one({"user_id": user_id})
        if not cart: 
            return None
        return asdict(cart)