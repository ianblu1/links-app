from flask import Blueprint, request, redirect, render_template, url_for
from flask import json
from flask.views import MethodView
from linksApp.models import Link
from linksApp import app

@app.route('/api_test')
def api_test():
    if 'name' in request.args:
        return 'Hello ' + request.args['name'] + '\n'
    else:
        return('Don\'t know who you are.\n')
    
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
    
@app.route('/data/bookmarks', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_data():
    if request.method=='GET':
        links=Link.objects.all()
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

#@app.route('/data/<slug>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
@app.route('/data/<slug>', methods=['GET', 'POST', 'DELETE'])
def api_bookmark(slug):
    #print(slug)
    if request.method=='GET':
        try:
            link=Link.objects.get(slug=slug)
            data=link.to_json()
            return data
        except:
            return "no such item\n"
        
    if request.method=='POST':
        link=Link.objects.get(slug=slug)
        data=request.json
        #tags=[]
        #for tag in data['tags'].split(','):
        #    tags.append(tag)
        #link.tags=tags
        link.tags=[tag for tag in data['tags'].split(',')]
        link.save()  
        
    if request.method=='DELETE':
        link=Link.objects.get(slug=slug)
        link.delete()
        return 'Success\n'

@app.route('/data', methods=['POST'])
def api_addItem():
    if request.method=='POST':                
        print("Got Here")
        data=request.json
        print(data)
        slug=data['title'].replace(' ', '-').replace(':', '')
        print(slug)
        check=Link.objects(slug=slug)
        print(len(check))
        if len(check)>0:
            return "link already exists\n"
        else:
            link=Link()
            link.slug=slug
            link.title=data['title']
            link.url=data['url']
            link.tags=[tag for tag in data['tags'].split(',')]
            link.save()
            return 'Success\n'
