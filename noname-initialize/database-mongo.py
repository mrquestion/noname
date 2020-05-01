import pymongo

import datetime
import hashlib

import settings

with pymongo.MongoClient(settings.database_mongo_host) as connection:
  database = connection.admin
  users = database.system.users
  if users.find_one(dict(user=settings.database_mongo_user)) is None:
    database = connection.noname
    database.command("createUser", settings.database_mongo_user, pwd=settings.database_mongo_pwd, roles=[ "readWrite" ])

def create_hash(key, secret):
  plaintext = ':'.join((settings.hash_key, key, secret))
  bs = plaintext.encode()
  return hashlib.sha512(bs).hexdigest()

with pymongo.MongoClient(**settings.database_mongo) as connection:
  print(connection.server_info())
  database = connection.noname

  now = datetime.datetime.utcnow().timestamp()

  nonames = database.nonames
  nonames_initialize_data = [
    dict(k="noname", n="noname", h=create_hash("noname", settings.noname_secret), ct=0, ut=0, lt=0, f=[ "default" ]),
    dict(k="test", n="<n:n:test>", h=create_hash("test", settings.test_secret), ct=0, ut=0, lt=0, f=[ "default" ]),
  ]
  if nonames.estimated_document_count() < len(nonames_initialize_data):
    nonames.insert_many(nonames_initialize_data)
  print(nonames.name, nonames.estimated_document_count())

  themes = database.themes
  themes_initialize_data = [
    dict(k="notice", n="<t:n:notice>", d="<t:d:notice>", nk="noname", nn="noname", ct=0, ut=0, f=[ "default", "enable" ]),
    dict(k="vote", n="<t:n:vote>", d="<t:d:vote>", nk="noname", nn="noname", ct=0, ut=0, f=[ "default", "enable" ]),
    dict(k="free", n="<t:n:free>", d="<t:d:free>", nk="noname", nn="noname", ct=0, ut=0, f=[ "default", "enable" ]),
  ]
  if themes.estimated_document_count() < len(themes_initialize_data):
    themes.insert_many(themes_initialize_data)
  print(themes.name, themes.estimated_document_count())

  pieces = database.pieces
  pieces_initialize_data = [
    dict(tk="notice", k="hello", t="<p:t:hello>", c="<p:c:hello>", nk="noname", nn="noname", ct=0, ut=0, f=[ "pin" ]),
  ]
  if pieces.estimated_document_count() < len(pieces_initialize_data):
    pieces.insert_many(pieces_initialize_data)
  print(pieces.name, pieces.estimated_document_count())

  dusts = database.dusts
  dusts_initialize_data = [
  ]
  if dusts.estimated_document_count() < len(dusts_initialize_data):
    dusts.insert_many(dusts_initialize_data)
  print(dusts.name, dusts.estimated_document_count())

  print(connection.list_database_names())
  print(database.list_collection_names())
