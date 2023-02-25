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
        
        price = 0
        for cart_product in cart.products:
            if not isinstance(cart_product, dict):
                cart_product = cart_product.__dict__
            price += (cart_product["quantity"] * cart_product["price"])
        cart.price = price
        cart.update()
        return asdict(cart)

    def remove_from_cart(self, user_id: str, product_id: str, size):
        cart = Cart.find_one({"user_id": user_id})
        if not cart:
            return CustomICCError.CART_NOT_FOUND
        index_to_pop = -1
        for idx, product in enumerate(cart.products):
            if product["parent"] == product_id and product["sizes"] == [size]:
                index_to_pop = idx
                break
        try:
            if index_to_pop == -1:
                return CustomICCError.CAN_NOT_REMOVE_FROM_CART
            cart.price -= (cart.products[index_to_pop].price * cart.products[index_to_pop].quantity)
            cart.products.pop(index_to_pop)
            cart.update()

            if len(cart.products) == 0:
                cart.delete()
            return asdict(cart)
        except IndexError as e:
            return CustomICCError.UNKNOWN_ERROR


    def get_cart_info(self, user_id: str):
        cart = Cart.find_one({"user_id": user_id})
        if not cart: 
            return None
        return asdict(cart)
    
    def _get_cart_by_id(self, cart_id):
        cart = Cart.find_one(cart_id)
        if not cart: 
            return None
        return cart