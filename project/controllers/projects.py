#!/usr/bin/env python

import time
import os

from project import app
from flask import Flask, Blueprint, render_template

projects = Blueprint('projects', __name__)


@app.route('/')
def index():
    body = 'welcome to appfog!'
    return render_template('main/index.html', body=body)


@app.route('/env')
def env():
    body = os.environ.get("VCAP_SERVICES", "{}")
    return render_template('main/mongo.html', body=body)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    full_file_name = file_name + '.txt'
    return app.send_static_file(full_file_name)


@app.errorhandler(404)
def page_not_found(e):
    return (render_template('errors/404.html'), 404)


@app.errorhandler(403)
def forbidden_page(e):
    return (render_template('errors/403.html'), 403)


@app.errorhandler(500)
def internal_server_error(e):
    return (render_template('errors/500.html'), 500)


@app.route('/mongo')
def mongotest():
    from pymongo import Connection
    from project.models.Model import Model
    model = Model()
    uri = model.mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return render_template('main/mongo.html', body=body)




