from flask import Blueprint, request
from utils.response_utils import compose_response
from controllers.crircbuzz import CricbuzzController


match_blueprint = Blueprint("match", __name__, url_prefix="/matches")


@match_blueprint.route("/", methods=["GET"])
def list_matches():
    match_id = request.args.get("match_id")
    if match_id:
        response = CricbuzzController.get_match_info(match_id)
        return compose_response(response)
    match_status = request.args.get("match_status", "recent")
    response = CricbuzzController.get_matches_list(match_status)
    return compose_response(response)