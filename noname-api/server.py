import flask

from . import settings

server = flask.Flask(__name__)

@server.route('/')
def index():
  return flask.jsonify(error=False)

@server.route("/version")
def _api_get_version():
  return flask.jsonify(error=False, version=settings.version)
