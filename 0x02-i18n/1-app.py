#!/usr/bin/env python3
""" script that instantiates babel """
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """ renders the index.html template """
    return render_template('1-index.html')

babel = Babel(app)
class Config(object):
    """class to configure languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
