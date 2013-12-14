# -*- coding: utf-8 -*-

MONGODB_CONFIG = {
    'HOST': '127.0.0.1',
    'PORT': 27017,
}

PHOTO_PATH = '/home/vagrant/var/diggit/upload/'
ICON_PATH = '/home/vagrant/var/diggit/icon/'

try:
    from local_settings import *
except:
    pass