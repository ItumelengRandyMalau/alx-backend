#!/usr/bin/env python3from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError
from flask import Flask, render_template, request, g

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale

    # Locale from user settings
    if g.user and g.user['locale'] and g.user['locale'] in ['en', 'fr']:
        return g.user['locale']

    # Locale from request header
    return request.accept_languages.best_match(['en', 'fr'])

@babel.timezoneselector
def get_timezone():
    # Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    # Default timezone
    return 'UTC'

@app.route('/')
def index():
    if g.user:
        return render_template('7-index.html', username=g.user["name"])
    return render_template('7-index.html', username=None)

if __name__ == '__main__':
    app.run(debug=True)
