import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
    """Return the homepage."""
    return render_template("homepage.html")

@app.route("/ISSlive")
def live():
    """Return the homepage."""
    return render_template("ISSlive.html")

@app.route("/predictionmap")
def predictionmap():
    """Return the homepage."""
    return render_template("predictionmap.html")

@app.route("/citiesdata")
def citiesdata():
    """Return the homepage."""
    return render_template("citiesdata.html")

@app.route("/tableau")
def tableau():
    """Return the homepage."""
    return render_template("tableau.html")

@app.route("/gallery")
def gallery():
    """Return the homepage."""
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run()

