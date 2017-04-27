'''
Common helper functions for all the classes in core.
'''

from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from flask import request

class ColumnsInspector(object):
	def __init__(self, obj):
		self.obj = obj

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

		return {x["attr_name"]: x for x in res}

	def get_convert(self, attr_type):
		converts = {
			Integer: int,
			String: str,
			DateTime: lambda x: datetime.strptime("%Y/%m/%d %H:%M:%S", x)
		}
		for sql_type, py_type in converts.items():
			if isinstance(attr_type, sql_type):
				return py_type
	
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

