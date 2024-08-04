#!/usr/bin/python3
"""
Index route for API version 1
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
