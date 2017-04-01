import json

from flask.views import MethodView
from flask import Blueprint

from app.models.data import Location, Session
from app.utils import format_keys
from app.core import get_all_queries

query_lister_handler = Blueprint('query_lister', __name__)

class QueryListerController(MethodView):
	def get(self):
		obj = get_all_queries()
		res = format_keys(obj.items(), (0, "name"), (1, "url"))
		return json.dumps(res), 200

query_lister_handler.add_url_rule('/queries/',
	view_func=QueryListerController.as_view('query_lister'))

