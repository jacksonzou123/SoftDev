from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hi, this is the homepage"

@app.route("/occupyflaskst")
def getjob():
    return render_template(
        'app.html',
        foo="fooooo",
        collection=coll
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
