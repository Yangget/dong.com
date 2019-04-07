import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://prople:prople@222.27.227.131:3306/people_count'
#SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost:5432/myapp'
#SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_RECYCLE = 3

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_FOLDER = 'translations'
LANGUAGES = {
    'en': {'flag': 'gb', 'name': 'English'},
    'pt': {'flag': 'pt', 'name': 'Portuguese'},
    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
    'es': {'flag': 'es', 'name': 'Spanish'},
    'fr': {'flag': 'fr', 'name': 'French'},
    'de': {'flag': 'de', 'name': 'German'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'ru': {'flag': 'ru', 'name': 'Russian'},
    'pl': {'flag': 'pl', 'name': 'Polish'},
    'el': {'flag': 'gr', 'name': 'Greek'},
    'ja_JP': {'flag': 'jp', 'name': 'Japanese'}
}


#------------------------------
# GLOBALS FOR GENERAL APP's
#------------------------------
UPLOAD_FOLDER = basedir + '/app/static/'
IMG_UPLOAD_FOLDER = basedir + '/app/static/'
IMG_UPLOAD_URL = '/static/'
AUTH_TYPE = 1
#AUTH_LDAP_SERVER = "ldap://dc.domain.net"
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'
APP_NAME = "People Flow Count"

# SQLALCHEMY_BINDS = {
# #     # 'my_sql1':'mysql://root:password@localhost/quickhowto',
#     'my_sql1':'mysql+pymysql://prople:prople@222.27.227.131:3306/people_count'
# }

# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# 绿色可以
# APP_THEME = "flatly.css"

# APP_THEME = "journal.css"

# 白色背景，黑色字体
APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"

# 蓝色
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"

# 同样浅蓝
# APP_THEME = "yeti.css"

