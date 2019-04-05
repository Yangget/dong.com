# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-5 下午5:32
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : index.py
"""
from flask_appbuilder import IndexView


class MyIndexView(IndexView):
    index_template = 'my_index.html'
