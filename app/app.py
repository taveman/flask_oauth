from functools import wraps

from flask import Flask, redirect, render_template, session
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

from configs.config import config
from logger.logger import log

app = Flask(__name__)
log.info('Starting up with the following configuration:\n%s', config)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=config.client_id,
    client_secret=config.client_secret,
    api_base_url=config.api_base_url,
    access_token_url=config.access_token_url,
    authorize_url=config.authorize_url,
    client_kwargs={
        'scope': 'openid profile email',
    },
)


def requires_auth(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/dashboard')


@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           user_data=session['jwt_payload'])


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='https://127.0.0.1:8008/callback')


@app.route('/logout')
def logout():

    # Clear session stored data
    session.clear()

    # Redirect user to logout endpoint
    params = {'returnTo': 'https://127.0.0.1:8008/', 'client_id': config.client_id}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))
