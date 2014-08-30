"""
Django settings for attsoc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import allModel
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cd3jpkn35=&(dwz9x(zh_+i#5igcg-!&kt*-e2+!w16j%i72z5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

STATICFILES_DIRS=(
                  os.path.join(BASE_DIR,'static','templates'),
                  )

TEMPLATE_DIRS=(
               
               os.path.join(BASE_DIR,'static','templates'),
               os.path.join(BASE_DIR,'static','templates','common'),
    #           "C:/Users/nuwan600/Documents/Aptana Studio 3 Workspace/attsoc_test4/static/templates",
               )

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages"
)

INSTALLED_APPS = (
    #'bootstrap_toolkit',
    #'javascript_settings',              
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'matplotlib',
    'pylab',
    'accounts',
    'surveys',
    'mails',
    'calender',
    'charts',
    'allModel',
    'organizations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'attsoc.urls'

WSGI_APPLICATION = 'attsoc.wsgi.application'

SESSION_SAVE_EVERY_REQUEST=True

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_AGE = 5*60

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

CSRF_FAILURE_VIEW=True

AUTH_PROFILE_MODULE='allModel.models.SuUser'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attsoc',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/templates/'
