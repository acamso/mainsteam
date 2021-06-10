# *- coding: utf-8 -*-
# basic_app.py
# 06-10-2021 18:41:52 EDT
# (c) 2021 acamso

"""Basic Flask application.

This is a Flask application to explore basic functionality. The app can be ran from
terminal using:

$ export FLASK_APP=basic_app
$ flask run
"""

from markupsafe import escape

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """Returns static HTML."""
    return "<div>Welcome</div>"

@app.route("/<name>")
def hello(name) -> str:
    """Returns escaped dynamic HTML.

    Dynamic HTML needs to be escaped to prevent injections.
    """
    return f"<div>Welcome, {escape(name)}</div>"
