from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from linksApp.models import Link
from linksApp import app

links = Blueprint('links', __name__, template_folder='templates')

class ListView(MethodView):

    def get(self):
        links = Link.objects.all()
        #print("got here")
        return render_template('links/list.html', link_objects=links)
    
    
# Register the urls
links.add_url_rule('/', view_func=ListView.as_view('list'))

