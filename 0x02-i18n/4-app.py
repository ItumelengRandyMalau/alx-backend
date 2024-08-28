#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if the locale parameter is in the URL
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale
    # Fall back to the best match if no locale parameter is provided
    return request.accept_languages.best_match(['en', 'fr'])
@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run()
