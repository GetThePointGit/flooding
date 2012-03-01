import logging
import os

# Set up logging BEFORE importing the base settings.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s %(levelname)s %(message)s')

from flooding.settings import *

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INSTALLED_APPS += ('debug_toolbar',)

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        #'HOST': '194.105.129.235',
#        'HOST': 'localhost',
#        'NAME': 'flooding21',
#        'USER': 'buildout',
#        'PASSWORD': 'buildout'
#        }
#    }

try:
    from flooding.localsettings import *
    # For local dev overrides.
except ImportError:
    pass

