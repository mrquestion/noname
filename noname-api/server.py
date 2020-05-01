import flask

import pymongo

from . import settings

server = flask.Flask(__name__)

@server.route('/')
def index():
  return flask.jsonify(error=False)

@server.route("/version")
def _api_get_version():
  return flask.jsonify(error=False, version=settings.version)

def _get(collection_name, query=None):
  with pymongo.MongoClient(**settings.database_mongo) as connection:
    database = connection.noname
    return database[collection_name].find(query)

@server.route("/nonames")
def _api_get_nonames():
  def normalize(nonames):
    for _noname in nonames:
      noname = dict(
        k=_noname["k"],
        n=_noname["n"],
        ct=_noname["ct"],
        lt=_noname["lt"],
      )
      if _noname.get("f", False):
        noname["f"] = _noname["f"]
      yield noname
  try:
    nonames = list(normalize(_get("nonames")))
    return flask.jsonify(error=False, nonames=nonames)
  except Exception as e:
    return flask.jsonify(error=True, message=e)
  return flask.jsonify(error=False)
