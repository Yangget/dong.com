import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from app.index import MyIndexView
"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# 导入Flask app对象
app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session ,indexview=MyIndexView)


from app import views,api

