"""
Django settings for IPZ project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gmnk)0^9d8!xnwa9n*$o8dh5q)jivhco@&myh79@$dzo^yyrsa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'registration',
    'profiles',
    'tinymce',
    #'south',
    'BrainStorm',
    'django.contrib.admindocs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'IPZ.urls'

WSGI_APPLICATION = 'IPZ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TEMPLATE_DIRS = (
"/home/yura/PycharmProjects/IPZ/templates",
)

STATICFILES_DIRS = (
    "/home/yura/PycharmProjects/IPZ",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-En'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'



STATIC_ROOT = "/home/yura/PycharmProjects/IPZ/static"

#AUTH_PROFILE_MODULE = 'IPZ.UserProfile'


MEDIA_ROOT = os.path.join(os.path.dirname('__file__'), '../media')
MEDIA_URL = '/media/'


USE_I18N

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

ACCOUNT_ACTIVATION_DAYS = 14

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@google.ru'

TEMPLATE_CONTEXT_PROCESSORS =(
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request",


)


TINYMCE_DEFAULT_CONFIG = {
    #'mode': "textareas",
    'theme': "advanced",
    'plugins': '''pagebreak, style, layer, table, save, advhr, advimage, advlink,
               emotions, iespell, inlinepopups, insertdatetime, preview, media,
               searchreplace, print, contextmenu, paste, directionality,
               fullscreen, noneditable, visualchars, nonbreaking, xhtmlxtras,
               template, wordcount, advlist, autosave''',

    'theme_advanced_buttons1': '''bold, italic, underline, strikethrough, |,
                               justifyleft, justifycenter, justifyright,
                               justifyfull, fontselect, fontsizeselect,
                               fullscreen, code''',
    'theme_advanced_buttons2': '''bullist, numlist, |, outdent, indent,
                               blockquote, |, undo, redo, |, link, unlink, |,
                               forecolor, backcolor''',
    'theme_advanced_buttons3': '''tablecontrols, |, hr, sub, sup, |, charmap''',

    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",

    'template_external_list_url': "lists/template_list.js",
    'external_link_list_url': "lists/link_list.js",
    'external_image_list_url': "lists/image_list.js",
    'media_external_list_url': "lists/media_list.js",

    'style_formats': [
      {'title': 'Bold text', 'inline': 'strong'},
      {'title': 'Red text', 'inline': 'span', 'styles': {'color' : '#ff0000'}},
      {'title': 'Help', 'inline': 'strong', 'classes': 'help'},
      {'title': 'Table styles'},
      {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow'}
    ],

    'width': '700',
    'height': '400'
}