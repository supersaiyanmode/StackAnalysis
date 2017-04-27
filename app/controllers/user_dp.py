import requests
from flask import Blueprint, Response, send_file

user_dp_handler = Blueprint('user_dp_handler', __name__)

@user_dp_handler.route("/users/<int:user_id>/dp")
def get_user_dp(user_id):
	url = "https://api.stackexchange.com/2.2/users/%d?&site=stackoverflow"%user_id
	image_url = requests.get(url).json()["items"][0]["profile_image"]
	resp = Response(requests.get(image_url).content)
	resp.headers["Content-Type"] = "image/jpeg"
	return resp


