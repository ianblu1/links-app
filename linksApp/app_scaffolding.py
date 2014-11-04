import os, datetime
from flask import current_app, Blueprint, render_template, abort, request, flash, redirect, url_for
from jinja2 import TemplateNotFound
from linksApp import login_manager, flask_bcrypt, app, forms
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)


app_scaffolding = Blueprint('app_scaffolding', __name__, template_folder='templates')

@app_scaffolding.route('/locked')
@login_required
def locked():
    return render_template('links/locked.html')
    
@app_scaffolding.route('/index')
@login_required
def hello():
    #if current_user:
    return render_template('links/hello.html')
    #else:
    #    return redirect('/login')
    
@app_scaffolding.route('/app_loc')
@login_required
def app_loc():
    return render_template('links/app_loc.html')  