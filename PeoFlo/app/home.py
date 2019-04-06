# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-6 下午4:42
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : home.py
"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_appbuilder import AppBuilder, expose, BaseView,has_access
from flask_appbuilder import IndexView

home = Blueprint('home', __name__,template_folder='templates/appbuilder')

class Home(IndexView):

    # @home.route('/volume/<input_volume>/')
    # @has_access
    def show(volumes):
        volumes = {1:"1111",2:"2222"}
        print(volumes)
        return volumes
