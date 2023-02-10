import json
from utils.error import ICCError


def get_response_structure(status, code, data=None, message=None):
    response = {
        "status": status,
        "code": code,
        "data": data,
        "message": message 
    }
    response = json.dumps(response, default=str)
    return response


def compose_response(obj, code=200,message=None):
    if isinstance(obj, ICCError):
        return get_response_structure(status=False, code=obj.error_code, message=obj.error_message)
    return get_response_structure(status=True, code=code, data=obj, message=message)