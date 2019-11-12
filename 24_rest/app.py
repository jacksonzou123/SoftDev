# Jackson Zou
# SoftDev1 PD 9
# K
#

from flask import Flask, render_template, request, redirect, url_for
import urllib.request as urllib2, json
app = Flask(__name__)

@app.route("/")
def hello_world():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=BAl9laaYBAEonY1OkUnpudItqDCgg4xxoIYVy1eU")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            pic = data["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
