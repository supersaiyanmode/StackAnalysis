import json

from flask import request
from sqlalchemy import desc
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.data import Base
from core.inspector import ColumnsInspector

class Sort(object):
	def __init__(self, obj):
		self.obj = obj
		self.inspector = ColumnsInspector(obj)
		self.cols = self.inspector.get_colums(obj)

	def parse_request(self, request):
		req = request.args.get('sort')
		if not req:
			return []

		return json.loads(req)

	def apply_order(self, obj, params):
		for param in params:
			col = param["col"]
			order = param["order"]
			col_data = self.cols[col]
			mapped_col = col_data["mapped_col"]

			if order == "desc":
				obj = obj.order_by(desc(mapped_col))
			elif order == "asc":
				obj = obj.order_by(mapped_col)

		return obj

	def order(self):
		params = self.parse_request(request)
		return self.apply_order(self.obj, params)

