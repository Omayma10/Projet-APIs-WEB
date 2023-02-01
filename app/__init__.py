#!/usr/bin/env python3
# -- coding: utf-8 --

from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask
from app import views
app = Flask(__name__)



