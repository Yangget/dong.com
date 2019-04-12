# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-5 下午1:34
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : forms.py
"""

# 现在定义表单视图以显示URL，创建菜单项，创建安全访问，定义前处理和后处理。
#
# 实现form_get和form_post以实现表单预处理和后处理。您可以使用form_get为您的数据预填充表单，
# 和/或预处理您的应用程序，然后使用form_post在用户提交表单后对表单进行处理，您可以将数据保存到数据库
# 发送电子邮件或任何其他需要采取的行动。
# from wtforms import Form, StringField
# from wtforms.validators import DataRequired
# from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
# from flask_appbuilder.forms import DynamicForm
#
#
# class MyForm(DynamicForm):
#     field1 = StringField(('Field1'),
#         description=('Your field number one!'),
#         validators = [DataRequired()], widget=BS3TextFieldWidget())
#     field2 = StringField(('Field2'),
#         description=('Your field number two!'), widget=BS3TextFieldWidget())
