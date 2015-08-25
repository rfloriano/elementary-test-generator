import dj_database_url
from .settings import *  # NOQA

ROOT_URLCONF = 'elementary_test_generator.elementary_test_generator.urls'

DATABASES['default'] = dj_database_url.config()

STATIC_URL = '/static/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
