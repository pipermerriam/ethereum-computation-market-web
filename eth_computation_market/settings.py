import os
import excavator as env
import dj_database_url
import django_cache_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('DJANGO_SECRET_KEY', required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DJANGO_DEBUG', type=bool, default=True)

TEMPLATE_DEBUG = DEBUG

# Template Locations
# https://docs.djangoproject.com/en/1.7/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'eth_computation_market', 'templates'),
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'eth_computation_market.apps.core.context_processors.rollbar',
)

ALLOWED_HOSTS = env.get('DJANGO_ALLOWED_HOSTS', type=list, required=not DEBUG)


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # third party
    'rest_framework',
    's3_folder_storage',
    'pipeline',
    'bootstrap3',
    'argonauts',
    # local project
    'eth_computation_market.apps.core',
    # local apps
    # django admin
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eth_computation_market.urls'

WSGI_APPLICATION = 'eth_computation_market.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.parse(env.get('DATABASE_URL', required=True)),
}
DATABASES['default'].setdefault('ATOMIC_REQUESTS', True)

# Cache
CACHES = {
    'default': django_cache_url.config(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static Files
STATIC_URL = env.get('DJANGO_STATIC_URL', default='/static/')
STATIC_ROOT = env.get(
    'DJANGO_STATIC_ROOT',
    default=os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = env.get('DJANGO_MEDIA_URL', default='/media/')
MEDIA_ROOT = env.get(
    'DJANGO_MEDIA_ROOT',
    default=os.path.join(BASE_DIR, 'media'),
)

DEFAULT_FILE_STORAGE = env.get(
    "DJANGO_DEFAULT_FILE_STORAGE",
    default="django.core.files.storage.FileSystemStorage",
)
STATICFILES_STORAGE = env.get(
    "DJANGO_STATICFILES_STORAGE",
    default="django.contrib.staticfiles.storage.StaticFilesStorage"
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'eth_computation_market', 'static'),
    os.path.join(BASE_DIR, 'bower_components'),
)

# Static file finders.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# Email Settings
EMAIL_BACKEND = env.get(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.smtp.EmailBackend',
)
EMAIL_HOST = env.get('EMAIL_HOST', default='localhost')
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = env.get('EMAIL_PORT', default='25')
EMAIL_USE_TLS = env.get('EMAIL_USE_TLS', type=bool)
EMAIL_USE_SSL = env.get('EMAIL_USE_SSL', type=bool)

# `django.contrib.sites` settings
SITE_ID = 1

# Sentry
RAVEN_CONFIG = {
    'dsn': env.get('SENTRY_DSN', default=None),
}

# Herokuify
SECURE_PROXY_SSL_HEADER = env.get('SECURE_PROXY_SSL_HEADER', type=list, default=None)

# AWS
AWS_ACCESS_KEY_ID = env.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.get('AWS_STORAGE_BUCKET_NAME')

DEFAULT_S3_PATH = "media"
STATIC_S3_PATH = "static"

# Sorl Thumbnailer
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
THUMBNAIL_FORMAT = 'PNG'

AWS_REDUCED_REDUNDANCY = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True
AWS_S3_SECURE_URLS = True
AWS_IS_GZIPPED = False
AWS_PRELOAD_METADATA = True
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}


if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    # Cached template loading is bad for dev so keep it off when debug is on.
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

# Django Pipeline Settings
PIPELINE = {
    'PIPELINE_ENABLED': env.get('DJANGO_PIPELINE_ENABLED', type=bool, required=not DEBUG),
    'DISABLE_WRAPPER': env.get(
        'DJANGO_PIPELINE_DISABLE_WRAPPER', type=bool, default=True,
    ),
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JAVASCRIPT': {
        'dependencies': {
            'source_filenames': (
                'jquery/dist/jquery.js',
                'tether/dist/js/tether.js',
                'bootstrap/dist/js/bootstrap.js',
                'prism/prism.js',
                'rollbar/dist/rollbar.js',
            ),
            'output_filename': 'js/dependencies.js',
        },
        'main': {
            'source_filenames': (
                'js/project.js',
                'js/prism-solidity.js',
            ),
            'output_filename': 'js/main.js',
        },
    },
    'STYLESHEETS': {
        'dependencies': {
            'source_filenames': (
                "bootstrap/dist/css/bootstrap.css",
                "font-awesome/css/font-awesome.css",
            ),
            'output_filename': 'css/dependencies.css',
        },
        'main': {
            'source_filenames': (
                "css/project.css",
            ),
            'output_filename': 'css/main.css',
        },
    }
}
