from flask import Flask
app = Flask(__name__) #creates a instance of the class

@app.route("/") #gives the route of the app, home directory
def hello_world():
    print(__name__)
    return "No hablo queso!"

@app.route("/yo")
def yo():
    print(__name__)
    return "Yo hablo queso!"

@app.route("/bleh")
def bleh():
    print(__name__)
    return "bleh"

@app.route("/num")
def num():
    ##print(__name__)
    return "num" #return type must be string

if __name__ == "__main__":
    app.debug = True
    app.run()

