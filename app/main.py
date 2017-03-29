from flask import Flask

from controllers import static_handler

class Main(object):
	def __init__(self, name=__name__):
		self.app = Flask(name)

	def register_module(self):
		self.app.register_blueprint(static_handler, url_prefix='')

	def server_start(self):
		self.app.run(host='0.0.0.0', threaded=True)

	def server_end(self):
		pass


if __name__ == '__main__':
	app = Main()
	app.server_start()
