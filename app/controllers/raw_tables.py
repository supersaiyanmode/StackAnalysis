import sys
import csv
import json

from flask import Blueprint
from flask.views import MethodView
from flask import jsonify
from flask import abort

from models.data import Session, Location, Tags, Users, Questions, Answers
from utils import format_attrs

raw_tables_handler = Blueprint('raw_tables_handler', __name__)


class RawTableController(MethodView):
	def get(self, id=None):
		if id is None:
			columns = [getattr(self.table, x) for x in self.input_fields]
			objects = Session.query(*columns).limit(10)

			args = zip(self.input_fields, self.output_fields)
			kwargs = {
				"preprocessors": getattr(self, "preprocessors", None),
				"postprocessors": getattr(self, "postprocessors", None),
			}
			response = format_attrs(objects, *args, **kwargs)
			return jsonify(**response)
		else:
			obj = Session.query(self.table).get(int(id))
			if obj is not None:
				return jsonify(**{x: getattr(obj, x) for x in self.input_fields})
			else:
				abort(404)

class UsersController(RawTableController):
	table = Users
	input_fields = ['id', 'name', 'reputation', 'location_id', 'views', 'upvotes',
						'downvotes', 'age']
	output_fields = ['ID', 'Name', 'Reputation', 'Location ID', 'Views', 'Upvotes',
						'Downvotes', 'Age']
	postprocessors = {
		"location_id": {
			"type": "link_replace",
			"url": "/locations/{{location_id}}/",
			"replace": "{{city}}, {{state}}, {{country}}",
		}
	}

class LocationController(RawTableController):
	table = Location
	input_fields = ['id', 'location', 'city', 'state', 'country', 'timezone']
	output_fields = ['ID', 'Location', 'City', 'State', 'Country', 'Timezone']

class TagsController(RawTableController):
	table = Tags
	input_fields = ['id', 'name']
	output_fields = ['ID', 'Name']

class QuestionsController(RawTableController):
	table = Questions
	input_fields = ['id', 'accepted_answer_id', 'score', 'author_id',
					'answer_count']
	output_fields = ['ID', 'Accepted Answer ID', 'Score', 'Author ID',
					'Answer Count']


class AnswersController(RawTableController):
	table = Answers
	input_fields = ['id', 'question_id', 'score', 'author_id']
	output_fields = ['ID', 'Question ID', 'Score', 'Author ID']


raw_tables_handler.add_url_rule( '/users/<int:id>/',
	view_func=UsersController.as_view('users_id'))
raw_tables_handler.add_url_rule( '/users/',
	view_func=UsersController.as_view('users'))

raw_tables_handler.add_url_rule( '/locations/<int:id>/',
	view_func=LocationController.as_view('locations_id'))
raw_tables_handler.add_url_rule( '/locations/',
	view_func=LocationController.as_view('locations'))

raw_tables_handler.add_url_rule( '/questions/<int:id>/',
	view_func=QuestionsController.as_view('questions_id'))
raw_tables_handler.add_url_rule( '/questions/',
	view_func=QuestionsController.as_view('questions'))

raw_tables_handler.add_url_rule( '/answers/<int:id>/',
	view_func=AnswersController.as_view('answers_id'))
raw_tables_handler.add_url_rule( '/answers/',
	view_func=AnswersController.as_view('answers'))

raw_tables_handler.add_url_rule( '/tags/<int:id>/',
	view_func=TagsController.as_view('tags_id'))
raw_tables_handler.add_url_rule( '/tags/',
	view_func=TagsController.as_view('tags'))

