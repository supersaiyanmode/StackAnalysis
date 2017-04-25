from collections import defaultdict

from flask import Blueprint
from flask import jsonify
from flask.views import MethodView
from flask_sqlalchemy_session import current_session as session

from models.data import ItemSets1, ItemSets2, Tags

tags_cluster_handler = Blueprint('tags_cluster_handler', __name__)

class TagsClusterController(MethodView):
	def get(self):
		tag_map = {x.id: x.name for x in session.query(Tags)}

		items1 = {x.tag: x.frequency for x in session.query(ItemSets1)}
		items2 = {(x.tag1, x.tag2): x.frequency for x in session.query(ItemSets2)}

		result = defaultdict(dict)
		for (t1, t2), freq in items2.iteritems():
			tag_name1 = tag_map[t1]
			tag_name2 = tag_map[t2]

			prob = float(freq) / items1[t2]
			if prob > 0.5:
				result[tag_name1][tag_name2] = {
					"combined_score": freq,
					"prob": float(freq) / items1[t2]
				}
		return jsonify(result=result)


tags_cluster_handler.add_url_rule('/tags_cluster/',
		view_func=TagsClusterController.as_view('tags_cluster'))
