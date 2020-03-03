# Jackson Zou, Saad Islam Bhuiyan
# SoftDev pd9
# K10 -- Import/Export Bank
# 2020-03-02


from pymongo import MongoClient
from bson.json_util import loads

def add_to_db( col , file ):
	f = open(file, "r")
	final = ""
	for line in f:
		final += line
	#print(final)
	final = loads(final)
	#print(final)
	col.insert(final)
	print("info gotten")

def getPlayerName( name, col ):
	pass

def getTeamName( name, col ):
	pass

def getConference( conference, col ):
	pass

def getDivision( division, col ):
	pass

def getPosition( position, col ):
	pass
