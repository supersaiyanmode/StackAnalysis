from operator import getitem

def format_response(obj, fn, *attrs):
	response = []
	out_fields = [x[1] if isinstance(x, tuple) else x for x in attrs]
	in_fields = [x[0] if isinstance(x, tuple) else x for x in attrs]
	for record in obj:
		cur_record = [fn(record, x) for x in in_fields]
		response.append(cur_record)
	return {
		"fields": out_fields,
		"data": response
	}

def format_attrs(obj, *attrs):
	return format_response(obj, getattr, *attrs)

def format_keys(obj, *attrs):
	return format_response(obj, getitem, *attrs)

