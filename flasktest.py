from flask import Flask
app = Flask(__name__) #creates a instance of the class

@app.route("/")
@app.route("/2") #gives the route of the app, home directory
def hello_world():
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()

