from datetime import datetime
import json

from flask import request
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.data import Base
from core.inspector import ColumnsInspector

class QueryFilter(object):
	def __init__(self, obj):
		self.obj = obj
		self.inspector = ColumnsInspector(obj)
		self.cols = self.inspector.get_colums(obj)

	def filter(self):
		params = self.parse_filter(request)
		return self.apply_filter(self.obj, params)

	def parse_filter(self, request):
		f = request.args.get('filter')
		if not f:
			return []

		return json.loads(f)

	def apply_filter(self, obj, params):
		for param in params:
			col = param["col"]
			operator = param["op"]
			operand = param["val"]
			col_data = self.cols[col]
			mapped_col = col_data["mapped_col"]
			
			if operand == "$$NONE$$" and operator in ('__eq__', '__ne__'):
				operand_converted = None
			else:
				operand_converted = col_data["convert"](operand)

			obj = obj.filter(getattr(mapped_col, operator)(operand_converted))
		return obj

	def filter_data(self):
		res = []
		for key, col_data in self.cols.items():
			res.append({
				"id": key,
				"text": col_data["attr_name"],
				"valid_ops": self.inspector.get_valid_ops(type(col_data["attr_type"]))
			})
		return res

