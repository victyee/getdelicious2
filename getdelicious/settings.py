"""
Django settings for getdelicious project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from .kunci import host, user, password, DJANGO_SECRET_KEY, AWS_SECRET_KEY, DB_PASSWORD

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
 
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'home',
    'products',
    'quotes',
    'contact',
    'owners',
    'pageviews',
    'django.contrib.sitemaps',
    'blog',
)

MIDDLEWARE_CLASSES = (
    # 'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pageviews.middleware.PageViewsMiddleware',
)

ROOT_URLCONF = 'getdelicious.urls'

WSGI_APPLICATION = 'getdelicious.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7t366tm92ltm0',
        'USER': 'viyrxwxvmldhso',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'ec2-23-23-81-221.compute-1.amazonaws.com'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static_files"),
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

AWS_ACCESS_KEY_ID = 'AKIAJZJ53MHDFTDECQMA'

AWS_SECRET_ACCESS_KEY = AWS_SECRET_KEY

AWS_STORAGE_BUCKET_NAME = 'getdelicious'

MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = ''

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Markdown
MARKDOWN_EDITOR_SKIN = 'simple'

#EMAIL SETTINGS
EMAIL_HOST = host
EMAIL_HOST_USER = user
EMAIL_HOST_PASSWORD = password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# To disable forced https
# SSLIFY_DISABLE = True