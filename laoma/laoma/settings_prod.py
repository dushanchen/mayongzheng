from .settings import *


import pymysql

pymysql.install_as_MySQLdb()

DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'laoma',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'Quattro!',
    }
}
  
