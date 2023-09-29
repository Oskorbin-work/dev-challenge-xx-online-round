""" This code executes:
1) Create Flask-app
"""
# Import flask Modules
from flask import Flask

# Creates Flask app
app = Flask(__name__)
# Tests flask
client = app.test_client()
# Disable sorting json-keys.
app.json.sort_keys = False
