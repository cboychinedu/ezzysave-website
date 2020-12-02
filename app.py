#!/usr/bin/env python3

# Importing the necessary modules
from time import sleep
from flask_cors import CORS, cross_origin
from flask import (Flask, jsonify, request,
                        render_template, redirect, url_for)

# Creating the flask application window
app = Flask(__name__)

# Setting the cross-origin acess
CORS(app)

# Creating the first route
@app.route("/")
def index():
    return render_template("index.html")


# Creating a route for the landing page
@app.route("/landing_page", methods=["POST", "GET"])
def landing_page():
    # Ensuring that the HTTP VERB is a post request.
    if request.method == "POST":
        sleep(2)
        return render_template("landing_page.html")

    # If a GET request, display error 404 page. 
    elif request.method == "GET":
        sleep(2)
        return render_template("404.html"), 404


    # Else/if not a post request, redirect the url to the homepage.
    else:
        return redirect(url_for('index'))


# Adding the error route
@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404



# Running the flask application
if __name__ == "__main__":
    app.run(debug=True)
