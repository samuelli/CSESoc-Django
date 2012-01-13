# Django settings for csesoc project.

import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

import csesoc_settings

if csesoc_settings.USE_REAL_EMAILS:
   CSESOC_SUGGEST_LIST = 'csesoc.suggestions@cse.unsw.edu.au'
   ADMINS = (
       ('Sysadmin Head', 'csesoc.sysadmin.head@csesoc.unsw.edu.au'),
   )
else:
   CSESOC_SUGGEST_LIST = csesoc_settings.MY_LOCAL_EMAIL
   ADMINS = (
       ('Sysadmin Head', csesoc_settings.MY_LOCAL_EMAIL),
   )

MANAGERS = ADMINS

FILE_UPLOAD_PERMISSIONS = 0644

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3')
    }
}

# Mail Settings
SMTP_HOST = 'smtp.unsw.edu.au'
SMTP_PORT = '25'
SEND_BROKEN_LINKS = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-AU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL where the django authentication login view is accessible
LOGIN_URL = "/accounts/login"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '../public/system')
#until we switch to using collectstatic, we use STATICFILES_DIRS and not STATIC_ROOT
#STATIC_ROOT = os.path.join(PROJECT_PATH, '../public/static')
STATICFILES_DIRS = (os.path.realpath(os.path.join(PROJECT_PATH, '../public/static')),)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://www.csesoc.unsw.edu.au/system/'
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = csesoc_settings.SETTINGS_SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request', # we need this to provide the request variable to each template
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'csesoc.context_processors.sponsors_list',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'csesoc.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
    os.path.join(PROJECT_PATH, 'templates/murder'),
    os.path.join(PROJECT_PATH, 'templates/game'),
    os.path.join(PROJECT_PATH, 'templates/suggestions'),
    os.path.join(PROJECT_PATH, 'templates/music'),
    os.path.join(PROJECT_PATH, 'templates/polls'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'csesoc.helpers',
    'csesoc.mainsite',    
    'csesoc.campleaders',
    'csesoc.campattendees',
    'csesoc.scheduler',
    'csesoc.sponsors',
    'csesoc.suggestions',
    'csesoc.murder',
    'csesoc.game',
    'csesoc.music',
    'csesoc.polls',
    'csesoc.paypal.standard.ipn',
    'csesoc.invoices',
)

AUTHENTICATION_BACKENDS = (
    'csesoc.auth.backends.CSEBackend',
    #'django.contrib.auth.backends.ModelBackend',
)

# maxiumum number of StreamItems per paginated index page
STREAMITEMS_PER_PAGE = 5

# Only ever set to true in Development, this will always be false on the live
# site because setting this variable to true activates a back door that allows
# anyone access to the admin site without a password or any form of
# verification.
ADMIN_NO_LOGIN = True

# django-paypal settings
PAYPAL_RECEIVER_EMAIL = "csesoc@cse.unsw.edu.au"
# Sandbox email:
#PAYPAL_RECEIVER_EMAIL = "razori_1326182346_biz@gmail.com"
SITE_DOMAIN = "http://www.csesoc.cse.unsw.edu.au/"
