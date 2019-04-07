from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db


from flask_appbuilder import AppBuilder, expose, BaseView,IndexView
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""


# 错误界面
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

# flask_appbuilder.security.decorators.has_access（f ）
# 使用此装饰器为您的方法启用粒度安全权限。权限将与角色相关联，角色与用户相关联
from flask_appbuilder import has_access

class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        return self.render_template("404.html")

    @expose('/method2/')
    @has_access
    def method2(self):
        return self.render_template("404.html")

    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        param1 = 'Goodbye %s' % (param1)
        return self.render_template('404.html',
                               param1=param1)


appbuilder.add_view(MyView(), "Method1", category='My View')
#appbuilder.add_view(MyView(), "Method2", href='/myview/method2/jonh', category='My View')
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("Method2", href='/myview/method2/jonh', category='My View')
# 请注意，这些方法将呈现未与FAB外观集成的简单页面。将方法的响应与应用程序的外观和感觉集成在一起很容易，
# 因此您必须创建自己的模板。在项目的目录和app文件夹下，创建一个名为“templates”的文件夹。
# 如在里面创建一个文件名'method3.html'
appbuilder.add_link("Method3", href='/myview/method3/jonh', category='My View')

# class IndexView(BaseView):
#
#     route_base = ''
#     default_view = 'index'
#     index_template = 'appbuilder/index.html'
#     base_permissions = ['can_list','can_show']
#
#     @expose('/')
#     @has_access
#     def index(self):
#         self.update_redirect()
#         return self.render_template(self.index_template,
#                                     appbuilder=self.appbuilder)
#
#     # @expose('/volume/<input_volume>/')
#     # # @has_access
#     # def show(volumes):
#     #     volumes = {}
#     #     print(volumes)
#     #     return volumes
