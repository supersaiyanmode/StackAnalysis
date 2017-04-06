import sys
import csv
import json

from flask import Blueprint
from flask.views import MethodView
from flask import jsonify
from flask_sqlalchemy_session import flask_scoped_session as session

from models.data import Location, Tags
from utils import format_keys

view_skills_locations_handler = Blueprint('tag_handler', __name__)

class ViewSkillsLocationsController(MethodView):
	def get(self):
		view_skill_rows = []
		tag_dict = self.tags_dict()
		path = "../data/view_skills_locations.csv"
		with open(path , "rb") as f:
			fl = csv.reader(f)
			for row in fl:
				row[3] = tag_dict.get(int(row[3]))
				view_skill_rows.append(row)
			response = format_keys(view_skill_rows,
							(1, 'country'), (2, 'state'), (0, 'city'),
							(3, 'skill'), (4, 'score'))
			return json.dumps(response)


	def tags_dict(self):
		return {r.id: r.name for r in  session.query(Tags.id, Tags.name).all()}


view_skills_locations_handler.add_url_rule('/view_skills_locations/',
				view_func=ViewSkillsLocationsController.as_view('view_skills_locations'))

