from flooding.settings import *

EXTERNAL_PRESENTATION_MOUNTED_DIR = (
    '/mnt/flooding/Flooding/presentationdatabase_totaal-staging')
EXTERNAL_RESULT_MOUNTED_DIR = '/mnt/flooding/Flooding/resultaten-staging'


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

RAVEN_CONFIG = {
    'dsn': 'https://133778d1860943c495d18dadea414c79:bfee15a67d1f45bc889e0ef47266e5e9@sentry.lizard.net/23',
}

try:
    from flooding.localstagingsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
