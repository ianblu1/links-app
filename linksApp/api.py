from flask import Blueprint, request, redirect, render_template, url_for
from flask import json
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
from jinja2 import TemplateNotFound
from linksApp.models import Link
from linksApp import app
import os, datetime

from libs.User import User

api_app = Blueprint('api_app', __name__, template_folder='templates')

@api_app.route('/data/bookmarks', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
@login_required
def api_data():
    if request.method=='GET':
        links=Link.objects.all()
        links=Link.objects(user=current_user.get_mongo_doc())
        print current_user.get_mongo_doc().email
        data=links.to_json()
        return(data)
    
    if request.method=='POST':
        if request.headers['Content-Type'] == 'application/json':
            bookmarks=request.json
            for bookmark in bookmarks:
                link=Link()
                print(bookmark['url'])
                link.url=bookmark['url']
                print(bookmark['title'])
                link.title=bookmark['title']
                link.slug=bookmark['title'].replace(' ', '-').replace(':', '')
                tags=[]
                for tag in bookmark['tags']:
                    tags.append(tag)
                print(tags)
                link.tags=tags
                link.save()
            return "JSON Message: SUCCESS"
        else:
            return "415 Unsupported Media Type ;)"

@api_app.route('/data/export', methods = ['GET'])
@login_required
def api_export_data():
    if request.method=='GET':
        links=Link.objects.all()
        data=links.to_json()
        #data=links
        print(links[1]["slug"])
        with open('seed_data/data.json', 'w') as outfile:
            #json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
            outfile.write(data)
        return "Success!\n"

#@app.route('/data/<slug>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
@api_app.route('/data/<slug>', methods=['GET', 'POST', 'DELETE'])
@login_required
def api_bookmark(slug):
    #print(slug)
    if request.method=='GET':
        try:
            link=Link.objects.get(slug=slug,user=current_user.get_mongo_doc())
            data=link.to_json()
            return data
        except:
            return "no such item\n"
        
    if request.method=='POST':
        link=Link.objects.get(slug=slug,user=current_user.get_mongo_doc())
        data=request.json
        #tags=[]
        #for tag in data['tags'].split(','):
        #    tags.append(tag)
        #link.tags=tags
        link.tags=[tag for tag in data['tags'].split(',')]
        link.save()  
        
    if request.method=='DELETE':
        link=Link.objects.get(slug=slug,user=current_user.get_mongo_doc())
        link.delete()
        return 'Success\n'

@api_app.route('/data', methods=['POST'])
@login_required
def api_addItem():
    if request.method=='POST':                
        print("Got Here")
        data=request.json
        print(data)
        slug=data['title'].replace(' ', '-').replace(':', '')
        print(slug)
        check=Link.objects(slug=slug,user=current_user.get_mongo_doc())
        print(len(check))
        if len(check)>0:
            return "link already exists\n"
        else:
            link=Link()
            link.slug=slug
            link.title=data['title']
            link.url=data['url']
            link.tags=[tag for tag in data['tags'].split(',')]
            link.user = current_user.get_mongo_doc()
            link.save()
            return 'Success\n'
