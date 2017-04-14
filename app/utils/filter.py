from datetime import datetime
import json

from flask import request
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.data import Base

class QueryFilter(object):
	def __init__(self, obj):
		self.obj = obj
		self.cols = self.get_colums(obj)

	def filter(self):
		params = self.parse_filter(request)
		return self.apply_filter(self.obj, params)

	def get_colums(self, obj):
		res = []

		for col in obj.cte().columns:
			table_name = col.base_columns.pop().table.name
			attr_name = col.name
			attr_type = col.type
			table_cls = self.get_table_class(table_name)
			convert = self.get_convert(attr_type)
			res.append({
				"table_name": table_name,
				"attr_name": attr_name,
				"attr_type": attr_type,
				"table_cls": table_cls,
				"convert": convert,
			})

		return {x["table_name"] + "." + x["attr_name"]: x for x in res}

	def get_table_class(self, name):
		for c in Base._decl_class_registry.values():
			if hasattr(c, '__table__') and c.__tablename__ == name:
				return c

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
			mapped_col = getattr(col_data["table_cls"], col_data["attr_name"])

			if operand == "$$NONE$$" and operator in ('__eq__', '__ne__'):
				operand_converted = None
			else:
				operand_converted = col_data["convert"](operand)

			obj = obj.filter(getattr(mapped_col, operator)(operand_converted))
		return obj

	def get_convert(self, attr_type):
		converts = {
			Integer: int,
			String: str,
			DateTime: lambda x: datetime.strptime("%Y/%m/%d %H:%M:%S", x)
		}
		for sql_type, py_type in converts.items():
			if isinstance(attr_type, sql_type):
				return py_type

	def filter_data(self):
		res = []
		for key, col_data in self.cols.items():
			res.append({
				"id": key,
				"text": col_data["table_cls"].__name__ + ", " + col_data["attr_name"],
				"valid_ops": self.get_valid_ops(type(col_data["attr_type"]))
			})
		return res

	def get_valid_ops(self, typ):
		return {
			Integer: [
				{"id": "__eq__", "text": "Equals ($$NONE$$ for null)"},
				{"id": "__lt__", "text": "Less Than"},
				{"id": "__le__", "text": "Less Than or Equal To"},
				{"id": "__gt__", "text": "Greater Than"},
				{"id": "__ge__", "text": "Greater Than or Equal To"},
				{"id": "__ne__", "text": "Not Equal To"},
			],
			String: [
				{"id": "like", "text": "SQL Like"},
				{"id": "__eq__", "text": "Equals ($$NONE$$ for null)"},
				{"id": "__ne__", "text": "Not Equal To"},
			],
			DateTime: [
				{"id": "__eq__", "text": "Equals ($$NONE$$ for null)"},
				{"id": "__lt__", "text": "Less Than"},
				{"id": "__le__", "text": "Less Than or Equal To"},
				{"id": "__ge__", "text": "Greater Than or Equal To"},
				{"id": "__ne__", "text": "Not Equal To"},
			],
		}.get(typ)


