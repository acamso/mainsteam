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
def static_route() -> str:
    """Returns static HTML."""
    return "<div>Welcome</div>"


@app.route("/<name>")
def dynamic_route(name) -> str:
    """Returns escaped dynamic HTML.

    This is an example of a dynamic route with a variable. The output is dynamic, so it needs to be
    escaped to prevent injections.
    """
    return f"<div>Welcome, {escape(name)}</div>"
