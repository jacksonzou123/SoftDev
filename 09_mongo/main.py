#Jackson Zou
#SoftDev pd9
#K09 -- Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from parse import parseData, getRestaurantsByBorough, getRestaurantsByZip, getRestaurantsByZipandGrade, getRestaurantsByZipandScore
client = MongoClient()
db = client["restaurants"]
print(db)

parseData(db, "primer-dataset.json")
getRestaurantsByZipandScore(db, "10024", "3")
getRestaurantsByZipandGrade(db, "10024", "B")
getRestaurantsByZip(db, "10024")
getRestaurantsByBorough(db, "Brooklyn")

