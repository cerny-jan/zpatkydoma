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

#  If the header is set to DENY then the browser will block the resource from loading in a frame no matter which site made the request.
X_FRAME_OPTIONS = 'DENY'

# If your Django app is behind a proxy, though, the proxy may be “swallowing” the fact that a request is HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#  SecurityMiddleware redirects all non-HTTPS requests to HTTPS (except for those URLs matching a regular expression listed in SECURE_REDIRECT_EXEMPT).
SECURE_SSL_REDIRECT = True

# sets the X-XSS-Protection: 1; mode=block header on all responses that do not already have it.
SECURE_BROWSER_XSS_FILTER = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
        'SEARCH_CONFIG': 'english',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URL', 'redis://127.0.0.1:6379'),
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
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True


# media files
GS_BUCKET_NAME = 'zpatkydoma'
GS_PROJECT_ID=os.getenv('GOOGLE_PROJECT_ID')
GOOGLE_SERVICE_ACCOUNT_INFO = os.getenv('GOOGLE_SERVICE_ACCOUNT_INFO')
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
    json.loads(GOOGLE_SERVICE_ACCOUNT_INFO))
GS_CACHE_CONTROL = 'public, max-age=604800'

INSTALLED_APPS += ['storages', 'wagtail.contrib.postgres_search']
MEDIA_URL = 'https://storage.googleapis.com/{bucket_name}/'.format(
    bucket_name=GS_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.eu'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')


TRACKING_ENVIRONMENT = 'staging'

try:
    from .local import *
except ImportError:
    pass
