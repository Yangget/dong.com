# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-5 下午5:32
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : index.py
"""
from flask_appbuilder import BaseView, expose, has_access


class IndexView(BaseView):

    route_base = ''
    default_view = 'index'
    index_template = 'appbuilder/index.html'
    base_permissions = ['can_list','can_show']

    @expose('/')
    @has_access
    def index(self):
        self.update_redirect()
        return self.render_template(self.index_template,
                                    appbuilder=self.appbuilder)

    # @expose('/volume/<input_volume>/')
    # # @has_access
    # def show(volumes):
    #     volumes = {}
    #     print(volumes)
    #     return volumes
