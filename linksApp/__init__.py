from flask import Flask, render_template, request, make_response
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt



app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "links_app"}
app.config["SECRET_KEY"] = "changeme"

app.url_map.strict_slashes = False

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine

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

#@app.route('/')
#def home():
#    from linksApp.models import Link
#    links = Link.objects.all()
#    for link in links:
#        print(link.title)
#    names=[links[0].title, links[1].title]
#    return render_template('links/list.html', link_objects=links)

#import linksApp.api

#@app.route('/')
#def basic_page():
#    return make_response(open('linksApp/templates/index.html').read())  

if __name__ == '__main__':
    app.run(debug=TRUE)