'''
Specifies the view , icon and related javascript page for each view.
'''

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
			"hashurl": "/",
			"view": "/static/views/dashboard/page.html",
			"icon": "dashboard",
			"sub": {}
		},
		{
			"text": "User Details",
			"hashurl": "/user-details/{id}",
			"hashparam": True,
			"view": "/static/views/user_details/page.html",
			"icon": "user",
			"sub": {
				"title": "User Details",
				"javascript": "/static/views/user_details/main.js"
			}
		},
		{
			"text": "Users",
			"hashurl": "/users",
			"view": "/static/views/generic.html",
			"icon": "users",
			"sub": {
				"title": "Users",
				"javascript": "/static/views/users/main.js"
			}
		},
		{
			"text": "Questions",
			"hashurl": "/questions",
			"view": "/static/views/generic.html",
			"icon": "question-circle",
			"sub": {
				"title": "Questions",
				"javascript": "/static/views/questions/main.js"
			}
		},
		{
			"text": "Answers",
			"hashurl": "/answers",
			"view": "/static/views/generic.html",
			"icon": "comments",
			"sub": {
				"title": "Answers",
				"javascript": "/static/views/answers/main.js"
			}
		},
		{
			"text": "Locations",
			"hashurl": "/locations",
			"view": "/static/views/generic.html",
			"icon": "map-marker",
			"sub": {
				"title": "Locations",
				"javascript": "/static/views/locations/main.js"
			}
		},
		{
			"text": "Tags",
			"hashurl": "/tags",
			"view": "/static/views/generic.html",
			"icon": "tags",
			"sub": {
				"title": "Tags",
				"javascript": "/static/views/tags/main.js"
			}
		},
		{
			"text": "Skill Distribution",
			"hashurl": "/skills-distribution",
			"view": "/static/views/generic.html",
			"icon": "globe",
			"sub": {
				"title": "Skill Distribution",
				"javascript": "/static/views/view_skills_locations/main.js"
			}
		},
		{
			"text": "Time Distribution",
			"hashurl": "/time-distribution",
			"view": "/static/views/generic.html",
			"icon": "clock-o",
			"sub": {
				"title": "Time Distribution",
				"javascript": "/static/views/view_answers_local_time/main.js"
			}
		},
		{
			"text": "Posts Count Distribution",
			"hashurl": "/posts-count-distribution",
			"view": "/static/views/generic.html",
			"icon": "clipboard",
			"sub": {
				"title": "Time Distribution",
				"javascript": "/static/views/view_posts_count_locations/main.js"
			}
		},
		{
			"text": "Average Score Distribution",
			"hashurl": "/average-score-distribution",
			"view": "/static/views/generic.html",
			"icon": "star-half-o",
			"sub": {
				"title": "Average Distribution",
				"javascript": "/static/views/view_average_score_locations/main.js"
			}
		},
		{
			"text": "Reputation v/s Fake Location",
			"hashurl": "/true-locations",
			"view": "/static/views/generic.html",
			"icon": "bar-chart",
			"sub": {
				"title": "Reputation v/s Fake Location",
				"javascript": "/static/views/true_location_reputation/main.js"
			}
		},
		{
			"text": "Tags Cluster",
			"hashurl": "/tags-cluster",
			"view": "/static/views/tagscluster/page.html",
			"icon": "tags",
			"sub": {},
		},
		{
			"text": "Users And Multiple Tags",
			"hashurl": "/multiple-tags",
			"view": "/static/views/generic.html",
			"icon": "users",
			"sub": {
				"title": "Users And Multiple Tags",
				"javascript": "/static/views/users_multiple_tags/main.js"
			}
		},
		{
			"text": "View Frequent Tags",
			"hashurl": "/frequent-tags",
			"view": "/static/views/view_frequent_tags/page.html",
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

