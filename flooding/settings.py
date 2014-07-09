# Base Django settings, suitable for production.  Imported (and partly
# overridden) by developmentsettings.py which also imports
# localsettings.py (which isn't stored in svn).
# Build19890150.1534fout takes care of using the correct one.  So:
# "DEBUG = TRUE" goes into developmentsettings.py and per-developer
# database ports go into localsettings.py.  May your hear turn purple
# if you ever put personal settings into this file or into
# developmentsettings.py!

import logging
import os
import tempfile
import matplotlib
matplotlib.use('Agg')

import sys
try:
    import PIL.Image
    sys.modules['Image'] = PIL.Image
except ImportError:
    import Image

from .settingshelper import setup_logging
from .settingshelper import STATICFILES_FINDERS

from pkg_resources import resource_filename

from logging.handlers import RotatingFileHandler

# SETTINGS_DIR allows media paths and so to be relative to this settings file
# instead of hardcoded to c:\only\on\my\computer.
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

# BUILDOUT_DIR is for access to the "surrounding" buildout, for instance for
# BUILDOUT_DIR/var/media files to give django-staticfiles a proper place
# to place all collected static files.
BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))

# Downloadable Excel files
EXCEL_DIRECTORY = os.path.join(BUILDOUT_DIR, "var", "excel")

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
        'HOST': 'p-flod-db-00-d1.external-nens.local',
        'NAME': 'flooding',
        'USER': 'flooding',
        'PASSWORD': 'XXXXX'  # See localproductionsettings.py
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
LANGUAGE_CODE = 'nl'
# For at-runtime language switching.  Note: they're shown in reverse order in
# the interface!
ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    ('nl', ugettext('Nederlands')),
)

LOCALE_PATHS = (os.path.join(BUILDOUT_DIR, 'src', 'flooding-lib', 'flooding_lib', 'locale'),)
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
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static')

MIDDLEWARE_CLASSES = (
    # Gzip needs to be at the top.
    #'django.middleware.gzip.GZipMiddleware',
    # Below is the default list, don't modify it.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
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
    'flooding_base',
    'flooding_presentation',
    'flooding_visualization',  # Must be below flooding_presentation
    'flooding_lib.tools.approvaltool',
    'lizard_worker',
    'lizard_raster',
    'flooding_lib',  # Must be below flooding_visualization,
                     # flooding_presentation, lizard_worker and
                     # approvaltool
    'flooding_lib.tools.importtool',
    'flooding_lib.tools.exporttool',
    'django.contrib.staticfiles',
    'south',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_extensions',
    'django_nose',  # Must be below south
    'supervisor',
    'gunicorn',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

LOGGING = setup_logging(
    BUILDOUT_DIR, console_level=None, file_level='WARN')

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

SYMBOLS_DIR = resource_filename(
    'flooding_visualization', 'media/flooding_visualization/symbols')
FLOODING_SHARE = '//p-isilon-d1.external-nens.local/nens/flooding/flod-share/'
EXTERNAL_PRESENTATION_MOUNTED_DIR = os.path.join(
    FLOODING_SHARE, 'presentationdatabase_totaal')
EXTERNAL_RESULT_MOUNTED_DIR = os.path.join(
    FLOODING_SHARE, 'resultaten')
TMP_DIR = os.path.join(
    FLOODING_SHARE, 'tmp_dir_used_by_site')

GIS_DIR = os.path.join(BUILDOUT_DIR, 'var', 'gisdata')

RASTER_SERVER_URL = "http://flooding.lizard.net/wms"

#location of directories for task execution. Pelase configure to local
#installation root of HIS schade en slachtoffers module
HISSSM_ROOT = ''
#root of sobek program installation
SOBEK_PROGRAM_ROOT = ''
#root of sobek projects
SOBEK_PROJECT_ROOT = ''
#root of temporary directory for flooding tasks
TMP_ROOT = 'c:/temp'

PERFORM_TASK_MODULE = "flooding_lib.tasks.perform_task"
PERFORM_TASK_FUNCTION = "perform_task"

#queue's setting for flooding-worke
QUEUES = {
    "default": {
        "exchange": "",
        "binding_key": "default"},
    "logging": {
        "exchange": "router",
        "binding_key": "logging"},
    "failed": {
        "exchange": "router",
        "binding_key": "failed"},
    "sort": {
        "exchange": "router",
        "binding_key": "sort"},
    "120": {
        "exchange": "router",
        "binding_key": "120"},
    "130": {
        "exchange": "router",
        "binding_key": "130"},
    "132": {
        "exchange": "router",
        "binding_key": "132"},
    "134": {
        "exchange": "router",
        "binding_key": "134"},
    "150": {
        "exchange": "router",
        "binding_key": "150"},
    "155": {
        "exchange": "router",
        "binding_key": "155"},
    "160": {
        "exchange": "router",
        "binding_key": "160"},
    "162": {
        "exchange": "router",
        "binding_key": "162"},
    "180": {
        "exchange": "router",
        "binding_key": "180"},
    "185": {
        "exchange": "router",
        "binding_key": "185"},
    "190": {
        "exchange": "router",
        "binding_key": "190"},
    "200": {
        "exchange": "router",
        "binding_key": "200"},
    "210": {
        "exchange": "router",
        "binding_key": "210"},
    "220": {
        "exchange": "router",
        "binding_key": "220"},
    "900": {
        "exchange": "router",
        "binding_key": "900"},
}

HEARTBEAT_QUEUES = ["120", "130", "132", "134", "150", "155", "160", "162", "180", "185", "190", "200", "210", "220"]

# TODO: configure your broker settings
# BROKER_SETTINGS = {
#     "BROKER_HOST": "localhost",
#     "BROKER_PORT": 5672,
#     "BROKER_USER": "",
#     "BROKER_PASSWORD": "",
#     "BROKER_VHOST": "flooding-test",
#     "HEARTBEAT": False
# }

# import ror-keringen
ROR_KERINGEN_PATH = os.path.join(BUILDOUT_DIR, 'var', 'ror_keringen')
ROR_KERINGEN_APPLIED_PATH = os.path.join(ROR_KERINGEN_PATH, 'applied')
ROR_KERINGEN_NOTAPPLIED_PATH = os.path.join(ROR_KERINGEN_PATH, 'not_applied')

try:
    from flooding.localproductionsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
