from flask import Blueprint
from flask.views import MethodView
from flask import jsonify

from models.data import Session, Location, Tags, Questions, Answers, Users
from utils import format_keys

overview_handler = Blueprint('overview_handler', __name__)

class OverviewController(MethodView):
	def get(self):
		users = Session.query(Users.id).count()
		tags = Session.query(Tags.id).count()
		questions = Session.query(Questions.id).count()
		answers = Session.query(Answers.id).count()
		locations = Session.query(Location.id).count()
		overview = {"data": [
			{
				"id": "questions",
				"text": "Questions",
				"color": "blue",
				"icon": "question-circle",
				"number": questions,
			},
			{
				"id": "answers",
				"text": "Answers",
				"color": "red",
				"icon": "comments",
				"number": answers,
			},
			{
				"id": "users",
				"text": "Users",
				"color": "green",
				"icon": "user",
				"number": users,
			},
			{
				"id": "locations",
				"text": "Locations",
				"color": "grey",
				"icon": "map-marker",
				"number": locations,
			},
			{
				"id": "tags",
				"text": "Tags",
				"color": "yellow",
				"icon": "tag",
				"number": tags,
			}
		]}
		obj = jsonify(**overview)
		obj.headers["cache-control"] = "max-age=86400"
		return obj
		
overview_handler.add_url_rule('/overview/',
	view_func=OverviewController.as_view('overview'))


		

