import json

from flask.views import MethodView
from flask import Blueprint
from flask import jsonify

from models.data import Location, Session
from utils import format_keys

view_lister_handler = Blueprint('view_lister', __name__)

VIEWS = {
	'data': [
		("Dashboard", "dashboard", "dashboard"),
		("Users", "users", "users"),
		("Questions", "questions", "question-circle"),
		
	]
}

class ViewListerController(MethodView):
	def get(self):
		return jsonify(**VIEWS)

view_lister_handler.add_url_rule('/views/',
	view_func=ViewListerController.as_view('view_lister'))

