#!/usr/bin/python3
""" init file for views blueprint. """

# from flask import Flask
from flask import Blueprint
# from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from models import storage
from api.v1.views.index import *
