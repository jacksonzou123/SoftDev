# Jackson Zou
# SoftDev1 PD 9
# K
#

from flask import Flask, render_template, request, redirect, url_for
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Start"

@app.route("/metaweather")
def metaweather():
    u = urllib.request.urlopen("https://www.metaweather.com/api/location/44418/")
    response = u.read()
    data = json.loads(response)
    weather = data['consolidated_weather'][0]
    print(data)
    return render_template("metaweather.html",
                            place = data['title'],
                            latt_long = data['latt_long'],
                            applicable_date = weather['applicable_date'],
                            weather_state_name = weather['weather_state_name'])

if __name__ == "__main__":
    app.debug = True
    app.run()
