#Jackson Zou
#SoftDev pd9
#K09 -- Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from bson.json_util import loads

#client = MongoClient()
#db = client["restaurants"]
#print(db)

def parseData( db, file ):
	f = open(file, "r")
	final = "["
	for line in f:
		line = line.strip()
		final += line + ","
	final = final[:len(final)-1] + "]"
	final = loads(final)
	db.restaurants.insert(final)
	print("info gotten")

def getRestaurantsByBorough( db, boro ):
	print("Restaurants in the borough of:", boro)
	info = db.restaurants.find( {"borough": boro} )
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZip( db, zip ):
	print("Restaurants with the zipcode of:", zip)
	info = db.restaurants.find( {"address.zipcode": zip})
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZipandGrade( db, zip, grade ):
	print("Restaurants with the zipcode and grade:", zip, grade)
	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.grade": grade})
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZipandScore( db, zip, score ):
	print("Restaurants with the zipcode and less score than:", zip, score)
	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.score": {"$lt": int(score)}})
	print(info)
	for stuff in info:
		print(stuff)

#parseData("primer-dataset.json")
#getRestaurantsByZipandScore("10024", "3")
#getRestaurantsByZipandGrade("10024", "B")
#getRestaurantsByZip("10024")
#getRestaurantsByBorough("Brooklyn")

