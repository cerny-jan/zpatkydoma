from __future__ import absolute_import, unicode_literals

import dj_database_url
from google.oauth2 import service_account
import json
from .base import *


DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

BASE_URL = 'https://intense-river-31481.herokuapp.com'

WAGTAILAPI_BASE_URL = 'https://intense-river-31481.herokuapp.com'

ALLOWED_HOSTS = ['intense-river-31481.herokuapp.com']

# client-side JavaScript will not to be able to access the CSRF cookie.
CSRF_COOKIE_HTTPONLY = True

# SecurityMiddleware sets the X-Content-Type-Options: nosniff header on all responses that do not already have it.
SECURE_CONTENT_TYPE_NOSNIFF = True

# the cookie will be marked as “secure,” which means browsers may ensure that the cookie is only sent with an HTTPS connection.
CSRF_COOKIE_SECURE = True
#
# Whether to use a secure cookie for the session cookie.
SESSION_COOKIE_SECURE = True
#
# X_FRAME_OPTIONS = 'Deny'
#
# If your Django app is behind a proxy, though, the proxy may be “swallowing” the fact that a request is HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#  SecurityMiddleware redirects all non-HTTPS requests to HTTPS (except for those URLs matching a regular expression listed in SECURE_REDIRECT_EXEMPT).
SECURE_SSL_REDIRECT = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ['REDIS_URL'],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
                'zpatkydoma.base.context_processors.custom_settings',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

# static files
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#
# COMPRESS_OFFLINE = True
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter',
# ]
# COMPRESS_CSS_HASHING_METHOD = 'content'

INSTALLED_APPS += ['compressor']

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'


# media files
GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME')
GS_PROJECT_ID=os.getenv('GOOGLE_PROJECT_ID')
GOOGLE_SERVICE_ACCOUNT_INFO = os.getenv('GOOGLE_SERVICE_ACCOUNT_INFO')
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
    json.loads(GOOGLE_SERVICE_ACCOUNT_INFO))


INSTALLED_APPS.append('storages')
MEDIA_URL = 'https://storage.googleapis.com/{bucket_name}/'.format(
    bucket_name=GS_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

TRACKING_ENVIRONMENT = 'staging'

try:
    from .local import *
except ImportError:
    pass
