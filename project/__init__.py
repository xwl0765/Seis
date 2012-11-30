#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'random'
app.debug = True

from project.controllers.projects import projects
app.register_blueprint(projects)