# *- coding: utf-8 -*-
# basic_app.py
# 06-10-2021 18:41:52 EDT
# (c) 2021 acamso

"""Basic Flask application."""

from __future__ import annotations

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return "<div>Welcome</div>"
