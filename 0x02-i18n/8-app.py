#!/usr/bin/ env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

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
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale
    if g.user and g.user['locale'] and g.user['locale'] in ['en', 'fr']:
        return g.user['locale']
    return request.accept_languages.best_match(['en', 'fr'])

@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    return 'UTC'

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)

@app.route('/')
def index():
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone)).strftime('%b %d, %Y, %I:%M:%S %p')
    if g.user:
        return render_template('8-index.html', username=g.user["name"], current_time=current_time)
    return render_template('8-index.html', username=None, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
