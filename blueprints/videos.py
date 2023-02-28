from flask import Blueprint, request
from controllers.videos import VideoController
from utils.response_utils import compose_response


videos_blueprint = Blueprint("videos", __name__)
vc = VideoController()

@videos_blueprint.route("/videos", methods=["GET"])
def list_videos():
    video_type = request.args.get("type")
    return compose_response(vc.list_videos(video_type))