from models.address import Address
from utils.error import CustomICCError

class AddressController:
    def add_address(self, user_id: str, address_obj: dict):
        address_obj["user_id"] = user_id
        address = Address.from_dict(address_obj)
        address.update()
        return address.get_dict()

    def update_address(self, user_id: str, address_obj: dict):
        address = Address.find_one(address_obj["_id"])
        if not address:
            return CustomICCError.ADDRESS_NOT_FOUND
        address.update_document_from_dict(address_obj)
        return address.get_dict()

    def delete_address(self, address_id: str):
        address = Address.find_one(address_id)
        if not address:
            return CustomICCError.ADDRESS_NOT_FOUND
        address.delete()
        return True

    def list_addresses(self, user_id: str):
        addresses = Address.find_many({"user_id": user_id})
        return [address.get_dict() for address in addresses]