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

version = "0.0.1"
secret_key = _settings.get("web", {}).get("secret_key", None)
api_url = _settings.get("api", {}).get("url", None)
