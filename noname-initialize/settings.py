import os
import json

def get_setting_filename():
  d, f = os.path.split(__file__)
  n, e = os.path.splitext(f)
  return os.path.join(d, os.extsep.join((n, "json")))

_setting_filename = get_setting_filename()
_settings = {}
if os.path.exists(_setting_filename):
  _settings.update(json.load(open(_setting_filename, "r")))

database_mongo = _settings.get("database-mongo", {})
database_mongo_host = database_mongo.get("host", None)
database_mongo_user = database_mongo.get("username", None)
database_mongo_pwd = database_mongo.get("password", None)
noname_secret = _settings.get("users", {}).get("noname", {}).get("secret", None)
test_secret = _settings.get("users", {}).get("test", {}).get("secret", None)
hash_key = _settings.get("hash_key", {})
