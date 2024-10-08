#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.context_processor
def inject_get_locale():
        return dict(get_locale=get_locale)

@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()
