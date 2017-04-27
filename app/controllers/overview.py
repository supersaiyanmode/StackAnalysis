from flask import Blueprint
from flask.views import MethodView
from flask import jsonify
from flask_sqlalchemy_session import current_session as session

from models.data import Location, Tags, Questions, Answers, Users
from core import format_keys

overview_handler = Blueprint('overview_handler', __name__)

class OverviewController(MethodView):
	def get(self):
		users = session.query(Users.id).count()
		tags = session.query(Tags.id).count()
		questions = session.query(Questions.id).count()
		answers = session.query(Answers.id).count()
		locations = session.query(Location.id).count()
		overview = {"data": [
			{
				"href": "/questions",
				"text": "Questions",
				"color": "blue",
				"icon": "question-circle",
				"number": questions,
			},
			{
				"href": "/answers",
				"text": "Answers",
				"color": "red",
				"icon": "comments",
				"number": answers,
			},
			{
				"href": "/users",
				"text": "Users",
				"color": "green",
				"icon": "user",
				"number": users,
			},
			{
				"href": "/locations",
				"text": "Locations",
				"color": "grey",
				"icon": "map-marker",
				"number": locations,
			},
			{
				"href": "/tags",
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

