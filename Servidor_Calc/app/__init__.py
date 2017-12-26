#!/usr/bin/python3.5
"""Initialization of the Flask app."""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
