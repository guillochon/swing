"""Flask server for Swing."""
import json
import logging
import os

import numpy as np

from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__)

# Define some globals here.

logger = logging.getLogger('gunicorn.error')
logger.setLevel(logging.INFO)


@app.route('/')
def index():
    """Return the index page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Return the about page."""
    return render_template('about.html')


@app.route('/data.json')
def data():
    return jsonify([
        {'District': 'GA-2',
         'Republican': 'Giant douche',
         'Democrat': 'Turd sandwich',
         'Funding Differential': '$0',
         'Importance': 'very'}
    ])


@app.route('/favicon.ico')
def favicon():
    """Return favicon."""
    return send_from_directory(
        os.path.join(app.root_path, 'static'), 'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


# This route ignored by nginx, only used locally.
@app.route('/<path:path>')
def send_file(path):
    """Send a file to the user."""
    print(path)
    return send_from_directory('', path)


def before_request():
    """Clear cache when HTML changes."""
    app.jinja_env.cache = {}


if __name__ == '__main__':
    app.before_request(before_request)
    app.run_server(debug=True)
