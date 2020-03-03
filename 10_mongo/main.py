# Jackson Zou, Saad Islam Bhuiyan
# SoftDev pd9
# K10 -- Import/Export Bank
# 2020-03-02

import pymongo, json, pprint
from bson.json_util import loads
from api import api_data_json
from parse import add_to_db

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['teamname'] # does not have to exist
col = db['nba']

if col.count() == 0:
	print('hello dere')
	api_data_json()
	add_to_db(col, "balldontlie.json")

answers = col.find({})
for line in answers:
	print(line)
