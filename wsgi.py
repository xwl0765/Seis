#!/usr/bin/env python

import os
import project
from flask import Flask
##from project import app

application = app = project.app

if __name__ == '__main__':
    app.run()