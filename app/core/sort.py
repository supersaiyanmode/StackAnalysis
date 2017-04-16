import json

from flask import request

from models.data import Base

class Sort(object):
	def __init__(self, obj):
		self.obj = obj

	def parse_request(self, request):
		req = request.args.get('sort')
		if not req:
			return []

		return json.loads(req)

	def get_colums(self, obj):
		res = []

		for col in obj.cte().columns:
			mapped_col = col.base_columns.pop()
			attr_name = col.description
			attr_type = col.type
			convert = self.get_convert(attr_type)
			res.append({
				"mapped_col": mapped_col,
				"attr_name": attr_name,
				"attr_type": attr_type,
				"convert": convert,
			})

def order(self):
		
