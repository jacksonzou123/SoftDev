# Jackson Zou
# SoftDev1 pd9
# Basic Flask Stuff
# 2019-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hi"

coll = [0,1,1,2,3,5,8]

if __name__ == "__main__":
    app.debug = True
    app.run()
