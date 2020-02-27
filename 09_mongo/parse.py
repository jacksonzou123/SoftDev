#Jackson Zou
#SoftDev pd9
#K09 -- Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()
db = client["restaurants"]
print(db)

def getData( file ):
	f = open(file, "r")
	final = "["
	for line in f:
		line = line.strip()
		final += line + ","
	final = final[:len(final)-1] + "]"
	final = loads(final)
	db.restaurants.insert(final)
	print(final)

getData("primer-dataset.json")
