#!/usr/bin/python3
"""
Flask App
"""

from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage


# Flask Application Variable: app
app = Flask(__name__)

# register the blueprint app_views
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    a method to handle @app.teardown_appcontext that calls storage.close()
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)


"""
host = environment variable HBNB_API_HOST or 0.0.0.0 if not defined
port = environment variable HBNB_API_PORT or 5000 if not defined
"""
if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
