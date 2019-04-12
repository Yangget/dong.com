# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-5 下午5:32
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : index.py
"""
from flask_appbuilder import BaseView, expose, has_access
from flask_appbuilder import IndexView


class MyIndexView(IndexView):


    # def index(self):
    #     self.update_redirect( )
    #     return self.render_template( self.index_template , appbuilder=self.appbuilder )

    index_template = 'index.html'
    @expose( "/" , methods=['POST', 'GET'])
    @has_access
    def index(self) :
        self.update_redirect( )
        return self.render_template( self.index_template , appbuilder=self.appbuilder )




