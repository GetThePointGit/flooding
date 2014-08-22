from .settingshelper import setup_logging

from flooding.settings import *

LOGGING = setup_logging(BUILDOUT_DIR)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '',
        'NAME': 'flooding',
        'USER': 'buildout',
        'PASSWORD': 'buildout'
        }
    }

RASTER_SERVER_URL = 'http://127.0.0.1:5000/wms'

RAVEN_CONFIG = {
}

try:
    from flooding.localsettings import *
    # For local dev overrides.
except ImportError:
    pass
