from flask import Flask
from flask_sqlalchemy_session import flask_scoped_session

from controllers import root_handler
from controllers import location_handler
from controllers import overview_handler
from controllers import raw_tables_handler
from controllers import view_lister_handler

from models.data import session_factory

class Main(object):
	def __init__(self, name=__name__):
		self.app = Flask(name)
		self.session = flask_scoped_session(session_factory, self.app)

	def register_modules(self):
		self.app.register_blueprint(root_handler, url_prefix='')
		self.app.register_blueprint(location_handler, url_prefix='')
		self.app.register_blueprint(overview_handler, url_prefix='')
		self.app.register_blueprint(raw_tables_handler, url_prefix='')
		self.app.register_blueprint(view_lister_handler,url_prefix='')

	def server_start(self):
		self.app.run(host='0.0.0.0', threaded=True)

	def server_end(self):
		pass


if __name__ == '__main__':
	app = Main()
	app.register_modules()
	app.server_start()
