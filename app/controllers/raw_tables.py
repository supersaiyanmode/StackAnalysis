import sys
import csv
import json

from flask import Blueprint
from flask.views import MethodView
from flask import jsonify

from models.data import Session, Location, Tags, Users, Questions, Answers
from utils import format_keys
from core import register_queries

raw_tables_handler = Blueprint('raw_tables_handler', __name__)


class RawTableController(MethodView):
	def get(self):
		columns = [getattr(self.table, x) for x in self.input_fields]
		output_format = zip(range(len(columns)), self.output_fields)
		objects = Session.query(*columns).limit(10)
		response = format_keys(objects, *output_format)
		return json.dumps(response)

class UsersController(RawTableController):
	table = Users
	input_fields = ['id', 'reputation', 'location_id', 'views', 'upvotes',
						'downvotes', 'age']
	output_fields = ['ID', 'Reputation', 'Location ID', 'Views', 'Upvotes',
						'Downvotes', 'Age']

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
					
raw_tables_handler = register_queries('RawTables', __name__,
				('users', '/users/', UsersController),
				('locations', '/locations/', LocationController),
				('tags', '/tags/', TagsController),
				('questions', '/questions/', QuestionsController),
				('answers', '/answers/', AnswersController))
