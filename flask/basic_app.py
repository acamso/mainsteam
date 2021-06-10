# *- coding: utf-8 -*-
# basic_app.py
# 06-10-2021 18:41:52 EDT
# (c) 2021 acamso

"""Basic Flask application.

This is a basic Flask application with a single route returning basic HTML. The app can be ran from
terminal using:

$ export FLASK_APP=basic_app
$ flask run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return "<div>Welcome</div>"
