import flask

import requests

from . import settings

server = flask.Flask(__name__, static_url_path='')
server.secret_key = settings.secret_key

@server.route('/')
def index(*args, **kwargs):
  return server.send_static_file("index.html")

@server.route("/index.html")
@server.route("/favicon.ico")
@server.route("/manifest.json")
def static_files():
  return server.send_static_file(flask.request.path[1:])

@server.route("/api/v<int:version>/<path:path>", methods=[ "HEAD", "PUT", "POST", "GET", "PATCH", "DELETE" ])
def api(version, path):
  request_data = {}
  if flask.request.values is not None:
    request_data.update(flask.request.values)
  if flask.request.json is not None:
    request_data.update(flask.request.json)
  response = requests.request(flask.request.method, f'{settings.api_url}/{path}', json=request_data)
  response_data = response.json()
  return flask.jsonify(response_data)
