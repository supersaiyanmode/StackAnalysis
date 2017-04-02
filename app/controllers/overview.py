import json

from flask import Blueprint
from flask.views import MethodView
from flask import jsonify

from models.data import Session, Location, Tags, Questions, Answers, Users
from utils import format_keys
from core import register_queries

overview_handler = Blueprint('overview_handler', __name__)

class OverviewController(MethodView):
	def get(self):
		users = Session.query(Users.id).count()
		tags = Session.query(Tags.id).count()
		questions = Session.query(Questions.id).count()
		answers = Session.query(Answers.id).count()
		locations = Session.query(Location.id).count()
		overview = {
			'users':users,
			'tags':tags,
			'questions':questions,
			'answers':answers,
			'locations':locations
		}
		return json.dumps(overview)
		
overview_handler.add_url_rule('/overview/',
	view_func=OverviewController.as_view('overview'))

		

