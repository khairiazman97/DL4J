# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
def hello():
    # this `return` is the response from our server. We are responding with the text "Hello World"
    return "Hello World!"