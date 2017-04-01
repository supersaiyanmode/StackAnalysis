import json

from flask.views import MethodView
from flask import Blueprint
from sqlalchemy import distinct

from app.models.data import Location, Session
from app.utils import format_attrs

location_handler = Blueprint('location_handler', __name__)

class CountryController(MethodView):
	def get(self):
		countries = Session.query(distinct(Location.country).label('country'))\
					.filter(Location.country != None)\
					.all()
		response = format_attrs(countries, ("country", "countries"))
		return json.dumps(response)

class StateController(MethodView):
	def get(self, country):
		states = Session.query(distinct(Location.state).label('state'))\
					.filter(Location.country == country)\
					.filter(Location.state != None)\
					.all()
		response = format_attrs(states, ("state", "states"))
		return json.dumps(response)

class CityController(MethodView):
	def get(self, country, state):
		cities = Session.query(distinct(Location.city).label('city'))\
					.filter(Location.country == country)\
					.filter(Location.state == state)\
					.filter(Location.city != None)\
					.all()
		response = format_attrs(cities, ("city", "cities"))
		return json.dumps(response)

location_handler.add_url_rule('/countries/',
				view_func=CountryController.as_view('countries'))
location_handler.add_url_rule('/countries/<country>/states/',
				view_func=StateController.as_view('states'))
location_handler.add_url_rule('/countries/<country>/states/<state>/cities/',
				view_func=CityController.as_view('cities'))
