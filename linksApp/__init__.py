from flask import Flask, render_template, request, make_response
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "links_app"}
app.config["SECRET_KEY"] = "changeme"

app.url_map.strict_slashes = False

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from linksApp.views import links
    app.register_blueprint(links)

#register_blueprints(app)

#@app.route('/')
#def home():
#    from linksApp.models import Link
#    links = Link.objects.all()
#    for link in links:
#        print(link.title)
#    names=[links[0].title, links[1].title]
#    return render_template('links/list.html', link_objects=links)

import linksApp.api

@app.route('/')
def basic_page():
    return make_response(open('linksApp/templates/index.html').read())

if __name__ == '__main__':
    app.run(debug=TRUE)