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
def dynamic_route(name: str) -> str:
    """Returns escaped dynamic HTML with provided name.

    This is an example of a dynamic route with a variable. Dynamic output needs to be escaped to prevent
    injections.
    """
    return f"<div>Welcome, {escape(name)}</div>"


@app.route("/id/<int:_id>")
def dynamic_route_w_type(_id: int) -> str:
    """Returns dynamic HTML with provided ID.

    This is an example of a dynamic route with a strict-type variable. Possible types are string, int,
    float, path, uuid. Incorrect type results in a 404 page.
    """
    assert isinstance(_id, int)
    return f"<div>The ID is {_id}</div>"
