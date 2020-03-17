# Jackson Zou
# SoftDev2 pd9
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-17

#We used the dataset from balldontlie api, and we got it by getting making api calls to get the json data for all of the players in the NBA
#After we gather the information from the api, we store it in a json file
#https://www.balldontlie.io/api/v1/players
#The data includes information about the players, including their name, position, and team info

import pymongo, json, pprint
from bson.json_util import loads
from api import api_data_json
from parse import add_to_db, getPlayerName, getTeamName, getConference, getDivision, getPosition
from flask import Flask, render_template, request
app = Flask(__name__)

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['teamname'] # does not have to exist
col = db['nba']

if col.count() == 0:
	print('hello dere')
	api_data_json()
	add_to_db(col, "balldontlie.json")

#answers = col.find({})
#for line in answers:
#	print(line)

#getPlayerName("James",col)
#getTeamName("Pacers", col)
#getConference("East", col)
#getDivision("Central", col)
#getPosition("C", col)
@app.route("/")
def home():
	return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
