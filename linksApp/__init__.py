from flask import Flask, render_template, request, make_response
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_sslify import SSLify
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
import os
#import config


app = Flask(__name__)

#app.config["MONGODB_SETTINGS"] = {'DB': "links_app"}
#app.config["SECRET_KEY"] = "changeme"
if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
#app.config["DEBUG"] = True
app.url_map.strict_slashes = False

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine
#app.config['MONGODB_SETTINGS'] = {'HOST':os.environ.get('MONGOLAB_URI'),'DB': 'FlaskLogin'}

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)

def register_blueprints(app):
    # Prevents circular imports
    #from linksApp.views import links
    from auth import auth_flask_login
    app.register_blueprint(auth_flask_login)
    from app_scaffolding import app_scaffolding
    app.register_blueprint(app_scaffolding)
    from api import api_app
    app.register_blueprint(api_app)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=TRUE)