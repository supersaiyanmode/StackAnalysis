from flask import request


class Paginator:
	def __init__(self, page_size):
		self.page_size = page_size

	def paginate(self, obj):
		page_num = self.extract_page_num(request)
		offset = (page_num) * self.page_size
		return obj.offset(offset).limit(self.page_size)

	def extract_page_num(self, request):
		return int(request.args.get('page', 0))

