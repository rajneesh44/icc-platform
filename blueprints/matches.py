from flask import Blueprint, request
from utils.response_utils import compose_response
from controllers.crircbuzz import CricbuzzController
from utils.error import CustomICCError


match_blueprint = Blueprint("match", __name__)


@match_blueprint.route("/matches", methods=["GET"])
def list_matches():
    match_id = request.args.get("match_id")
    if match_id:
        response = CricbuzzController.get_match_info(match_id)
        return compose_response(response)
    match_status = request.args.get("match_status", "recent")
    response = CricbuzzController.get_matches_list(match_status)
    return compose_response(response)

@match_blueprint.route("/icc-stats", methods=["GET"])
def get_icc_stats():
    category = request.args.get("category")
    format = request.args.get("format")
    if not (format and category):
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    response = CricbuzzController.get_icc_rankings(category, format)
    return compose_response(response)


@match_blueprint.route("/news", methods=["GET"])
def get_cricket_news():
    return compose_response(CricbuzzController.get_icc_news())


@match_blueprint.route("/search/player", methods=["GET"])
def search_player():
    name = request.args.get("name")
    if not name:
        return compose_response(CustomICCError.INVALID_PARAMS_OR_REQUIRED_PARAMS_MISSING)
    return compose_response(CricbuzzController.search_player(name))
