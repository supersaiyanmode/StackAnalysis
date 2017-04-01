from flask import Blueprint

queries = {}

def register_queries(bp_name, file_name, *args):
	bp = Blueprint(bp_name, file_name)
	for name, url, cls in args:
		bp.add_url_rule(url, view_func=cls.as_view(name))
		queries[name] = url
	return bp

def get_all_queries():
	return queries

