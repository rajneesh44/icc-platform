from controllers.instamojo import InstaMojoController
from controllers.cart import CartController
from utils.error import CustomICCError
from models.order import Order
from models.user import User

cc = CartController()

class OrderController:
    def create_order(self, user_id, cart_id):
        cart = cc._get_cart_by_id(cart_id)
        if not cart:
            return CustomICCError.CART_NOT_FOUND
        
        user = User.find_one(user_id)
        order_dict = {
            "cart_id": cart_id,
            "user_id": user_id,
            "price": cart.price,
        }
        order = Order.from_dict(order_dict)
        # order.update()

        payment_link = InstaMojoController.create_payment_request(
            cart.price, 
            "Purchase",
            send_email=False if user.phone_number else True,
            email=user.email if user.email else None,
            send_sms=False if user.email else True,
            phone_number=user.phone_number if user.phone_number else None,
            )
        order.payment_id = payment_link["id"]
        order.meta["payment_link"] = payment_link["longurl"]
        order.status = 1
        order.update()
        return order.__dict__
    
    def list_orders(self, user_id):
        orders = Order.find_many({"user_id": user_id})
        if not len(orders):
            return []
        return [order.__dict__ for order in orders]


            
