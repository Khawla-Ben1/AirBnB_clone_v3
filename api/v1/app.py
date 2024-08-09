#!/usr/bin/python3
"""
Flask application to serve the API
"""
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Teardown method to close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Handler for 404 errors that returns a JSON response """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host="0.0.0.0", port=5000, threaded=True)
