#!/usr/bin/env python3
from flask import Flask, render_template, request, g

app = Flask(__name__)

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

@app.route('/')
def index():
    if g.user:
        return render_template('5-index.html', username=g.user["name"])
    return render_template('5-index.html', username=None)

if __name__ == '__main__':
    app.run(debug=True)
