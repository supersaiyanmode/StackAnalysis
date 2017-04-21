from flask import Blueprint
from flask import jsonify
from flask.views import MethodView
from flask_sqlalchemy_session import current_session as session

from models.data import ItemSets1, ItemSets2, Tags

class TagsClusterController(MethodView):
	def get(self):
		tag_map = {x.id: x.name for x in session.query(Tags)}

		items1 = {x.tags1: x.frequency for x in session.query(ItemSets1)}
		items2 = {(x.tags1, x.tags2): x.frequency for x in session.query(ItemSets2)}

		
