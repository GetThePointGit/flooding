import logging
import os

# Set up logging BEFORE importing the base settings.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s %(levelname)s %(message)s')

from flooding.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '194.105.129.235',
        #'HOST': 'localhost',
        'NAME': 'flooding21',
        'USER': 'postgres',
        'PASSWORD': 'lizard123'
        }
    }

try:
    from flooding.localsettings import *
    # For local dev overrides.
except ImportError:
    pass

