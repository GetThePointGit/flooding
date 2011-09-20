# Base Django settings, suitable for production.
# Imported (and partly overridden) by developmentsettings.py which also
# imports localsettings.py (which isn't stored in svn).  Buildout takes care
# of using the correct one.
# So: "DEBUG = TRUE" goes into developmentsettings.py and per-developer
# database ports go into localsettings.py.  May your hear turn purple if you
# ever put personal settings into this file or into developmentsettings.py!

import logging
import os
import tempfile
import matplotlib
matplotlib.use('Agg')

import sys
import PIL.Image
sys.modules['Image'] = PIL.Image


from logging.handlers import RotatingFileHandler

# SETTINGS_DIR allows media paths and so to be relative to this settings file
# instead of hardcoded to c:\only\on\my\computer.
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

# BUILDOUT_DIR is for access to the "surrounding" buildout, for instance for
# BUILDOUT_DIR/var/media files to give django-staticfiles a proper place
# to place all collected static files.
BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))

# Triple blast.  Needed to get matplotlib from barfing on the server: it needs
# to be able to write to some directory.
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()

# Production, so DEBUG is False. developmentsettings.py sets it to True.
DEBUG = False
# Show template debug information for faulty templates.  Only used when DEBUG
# is set to True.
TEMPLATE_DEBUG = True

# ADMINS get internal error mails, MANAGERS get 404 mails.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '194.105.129.235',
        'NAME': 'flooding21',
        'USER': 'postgres',
        'PASSWORD': 'lizard123'
        }
    }


# Almost always set to 1.  Django allows multiple sites in one database.
SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems.  If running in a Windows
# environment this must be set to the same as your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'
# For at-runtime language switching.  Note: they're shown in reverse order in
# the interface!
LANGUAGES = (
    ('nl', 'Nederlands'),
)
# If you set this to False, Django will make some optimizations so as not to
# load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds user-uploaded media.
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'media')
# Absolute path to the directory where django-staticfiles'
# "bin/django build_static" places all collected static files from all
# applications' /media directory.
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected by
# django-staticfiles.  Use it in templates like
# "{{ MEDIA_URL }}mypackage/my.css".
STATIC_URL = '/static_media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.  Uses STATIC_URL as django-staticfiles nicely collects
# admin's static media into STATIC_ROOT/admin.
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Storage engine to be used during compression
###COMPRESS_STORAGE = "staticfiles.storage.StaticFileStorage"

# The URL that linked media will be read from and compressed media will be
# written to.
###COMPRESS_URL = STATIC_URL
# The absolute file path that linked media will be read from and compressed
# media will be written to.
###COMPRESS_ROOT = STATIC_ROOT

# django-staticfiles needs an extra context processor to allow you to use {{
# STATIC_URL }}myapp/my.css in your templates.
TEMPLATE_CONTEXT_PROCESSORS = (
    # Default items.
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    # Extra for django-staticfiles.
    'staticfiles.context_processors.static_url',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b8cdceb3-4879-4dcc-96ef-5030c2493fa0'

ROOT_URLCONF = 'flooding.urls'

CACHE_BACKEND = 'file://%s' % os.path.join(BUILDOUT_DIR, 'var', 'cache')
# Note: for development only, check django website for caching solutions for
# production environments
# ^^^ TODO

INSTALLED_APPS = (
    'flooding',
    'lizard_flooding',
    'lizard_presentation',
    'lizard_visualization',
    'lizard_flooding.tools.importtool',
    'lizard_flooding.tools.exporttool',
    'lizard_flooding.tools.approvaltool',
    'lizard_flooding-worker',
    'lizard_base',
    'staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
)

# File logging for production.  If logging is already defined (for instance in
# developmentsettings.py, this won't have any effect.
logging.basicConfig(
    level=logging.DEBUG,
    format = ('=' * 78 + '\n' +
              '%(asctime)s %(name)s %(levelname)s\n%(message)s'),
    filename=os.path.join(BUILDOUT_DIR, 'var', 'log', 'django.log'),
    filemode='a')

# We create a handler to be able to show the tail of the Django log to the
# user. The handler implements the tail through up to two log files that are
# each up to 4 KB large. The log files are called
#
#    - /var/log/django_tail.log and
#    - /var/log/django_tail.log.1
#
# The latter log file is only created when the former has reached its maximum
# size.
TAIL_LOG = os.path.join(BUILDOUT_DIR, 'var', 'log', 'django_tail.log')

handler = RotatingFileHandler(TAIL_LOG, maxBytes=4096, backupCount=1)
logging.getLogger().addHandler(handler)

SYMBOLS_DIR = 'C:/repo/flooding/local_checkouts/lizard-flooding/lizard_presentation/media/lizard_presentation/symbols/'
#EXTERNAL_MOUNTED_DIR = os.path.join(BUILDOUT_DIR, 'var', 'external_data')
GIS_DIR = 'C:/repo/gisdata/uiteindelijk/'

#location of directories for task execution. Pelase configure to local installation 
#root of HIS schade en slachtoffers module
HISSSM_ROOT=''
#root of sobek program installation
SOBEK_PROGRAM_ROOT=''
#root of sobek projects
SOBEK_PROJECT_ROOT=''
#root of temporary directory for flooding tasks
TMP_ROOT='c:/temp'

try:
    from flooding.localproductionsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
