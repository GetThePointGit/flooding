from flooding.settings import *

DEBUG = True

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': 'floodingtest',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'floodingtest',
        'PASSWORD': 'XXXXXX',  # See localstagingsettings.py
        'HOST': 'p-flod-db-00-d1.external-nens.local',
        'PORT': '',
        },
    }

try:
    from flooding.localstagingsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
