'''
Specifies the format of json response for each view. 
'''

from operator import getitem

def format_response(obj, fn, *attrs, **kwargs):
	preprocessors = kwargs.pop('preprocessors', {})
	postprocessors = kwargs.pop('postprocessors', [])

	response = []
	out_fields = [x[1] if isinstance(x, tuple) else x for x in attrs]
	in_fields = [x[0] if isinstance(x, tuple) else x for x in attrs]
	for record in obj:
		cur_record = [fn(record, x) for x in in_fields]
		response.append(cur_record)
	return {
		"fields": in_fields,
		"display": out_fields,
		"data": response,
		"mappers": postprocessors,
	}

def format_attrs(obj, *attrs, **kwargs):
	return format_response(obj, getattr, *attrs, **kwargs)

def format_keys(obj, *attrs, **kwargs):
	return format_response(obj, getitem, *attrs, **kwargs)

