# Jackson Zou
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-17


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

def printPlayer( item ):
	final = ""
	final += "Name: " + item['first_name'] + " " + item['last_name'] + " Team: " + item["team"]["full_name"] + "\n"
	return final

def getPlayerName( name, col ):
	final = []
	items = col.find({"first_name": name})
	for item in items:
		final.append(printPlayer( item ))
	return final

def getTeamName( name, col ):
	final = []
	items = col.find({"team.name": name})
	for item in items:
		final.append(printPlayer( item ))
	return final

def getConference( conference, col ):
	final = []
	items = col.find({"team.conference": conference})
	for item in items:
		final.append(printPlayer( item ))
	return final

def getDivision( division, col ):
	final = []
	items = col.find({"team.division": division})
	for item in items:
		final.append(printPlayer( item ))
	return final

def getPosition( position, col ):
	final = []
	items = col.find({"position": position})
	for item in items:
		final.append(printPlayer ( item ))
	return final
