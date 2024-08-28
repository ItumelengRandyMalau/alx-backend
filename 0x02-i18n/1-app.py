#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel, get_locale

class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)
