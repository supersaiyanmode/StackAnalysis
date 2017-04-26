import json

from flask.views import MethodView
from flask import Blueprint
from flask import jsonify

from models.data import Location
from core import format_keys

view_lister_handler = Blueprint('view_lister', __name__)

VIEWS = {
	'data': [
		{
			"text": "Dashboard",
			"view": "/static/views/dashboard/page.html",
			"icon": "dashboard",
			"sub": {}
		},
		{
			"text": "Users",
			"view": "/static/views/generic.html",
			"icon": "users",
			"sub": {
				"title": "Users",
				"javascript": "/static/views/users/main.js"
			}
		},
		{
			"text": "Questions",
			"view": "/static/views/generic.html",
			"icon": "question-circle",
			"sub": {
				"title": "Questions",
				"javascript": "/static/views/questions/main.js"
			}
		},
		{
			"text": "Answers",
			"view": "/static/views/generic.html",
			"icon": "comments",
			"sub": {
				"title": "Answers",
				"javascript": "/static/views/answers/main.js"
			}
		},
		{
			"text": "Locations",
			"view": "/static/views/generic.html",
			"icon": "map-marker",
			"sub": {
				"title": "Locations",
				"javascript": "/static/views/locations/main.js"
			}
		},
		{
			"text": "Tags",
			"view": "/static/views/generic.html",
			"icon": "tags",
			"sub": {
				"title": "Tags",
				"javascript": "/static/views/tags/main.js"
			}
		},
		{
			"text": "Skill Distribution",
			"view": "/static/views/generic.html",
			"icon": "globe",
			"sub": {
				"title": "Skill Distribution",
				"javascript": "/static/views/view_skills_locations/main.js"
			}
		},
		{
			"text": "Time Distribution",
			"view": "/static/views/generic.html",
			"icon": "clock-o",
			"sub": {
				"title": "Time Distribution",
				"javascript": "/static/views/view_answers_local_time/main.js"
			}
		},
		{
			"text": "Posts Count Distribution",
			"view": "/static/views/generic.html",
			"icon": "clipboard",
			"sub": {
				"title": "Time Distribution",
				"javascript": "/static/views/view_posts_count_locations/main.js"
			}
		},
		{
			"text": "Average Score Distribution",
			"view": "/static/views/generic.html",
			"icon": "star-half-o",
			"sub": {
				"title": "Average Distribution",
				"javascript": "/static/views/view_average_score_locations/main.js"
			}
		},
		{
			"text": "Reputation v/s Fake Location",
			"view": "/static/views/generic.html",
			"icon": "bar-chart",
			"sub": {
				"title": "Reputation v/s Fake Location",
				"javascript": "/static/views/true_location_reputation/main.js"
			}
		},
		{
			"text": "Tags Cluster",
			"view": "/static/views/tagscluster/page.html",
			"icon": "tags",
			"sub": {},
		},
		{
			"text": "Users And Multiple Tags",
			"view": "/static/views/generic.html",
			"icon": "users",
			"sub": {
				"title": "Users And Multiple Tags",
				"javascript": "/static/views/users_multiple_tags/main.js"
			}
		},
		{
			"text": "View Frequent Tags",
			"view": "/static/views/generic.html",
			"icon": "tasks",
			"sub": {
				"title": "View Frequent Tags",
				"javascript": "/static/views/view_frequent_tags/main.js"
			}
		}
	]
}

class ViewListerController(MethodView):
	def get(self):
		return jsonify(**VIEWS)

view_lister_handler.add_url_rule('/views/',
	view_func=ViewListerController.as_view('view_lister'))

