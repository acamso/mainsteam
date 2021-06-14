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

from typing import Optional

from markupsafe import escape

from flask import Flask, url_for

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


@app.route("/dir/")
def static_dir_route() -> str:
    """Returns plain text.

    This is an example of a static route with a trailing slash. The same path without a trailing slash
    redirects to this endpoint. Accessing a non-existing trailing slash endpoint results in a 404 page.
    """
    return "This is an endpoint with a trailing slash."


@app.route("/url/<name>")
def url(name: str) -> str:
    """Returns this dynamic relative URL in plain text."""
    return url_for("url", name=name)


@app.route("/abs_url/<name>")
def abs_url(name: str) -> str:
    """Returns this dynamic absolute URL in plain text."""
    return url_for("url", name=name, _external=True)


@app.route("/opt_id/<int:_id>")
@app.route("/opt_id/<int:_id>/<user>")
def opt_param(_id: int, user: Optional[str] = None) -> str:
    """Returns dynamic HTML with provided ID and the username if provided.

    This is an example of a dynamic route with an optional parameter.
    """
    res = f"<div>The ID is {_id}"
    if user:
        res += f" and the username is {user}"
    res += "</div>"
    return res
