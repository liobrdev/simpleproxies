from decouple import config, Csv
from email.utils import getaddresses
from pathlib import Path

import secret_django_settings as secrets


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secrets.SECRET_KEY
DEBUG = config('DEBUG', default=False, cast=bool)
DJANGO_ENV = config('DJANGO_ENV', default='production')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ADMINS = getaddresses(config('ADMINS', cast=Csv()))

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = secrets.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secrets.EMAIL_HOST_PASSWORD
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX') + ' '
SERVER_EMAIL = config('SERVER_EMAIL')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'django_user_agents',
    'rest_framework',
    'custom_db_logger',
    'proxies',
    'utils',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'simpleproxies_api.middleware.ClientIPMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

ROOT_URLCONF = 'simpleproxies_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simpleproxies_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets.DB_LOGGER_NAME,
        'USER': secrets.DB_LOGGER_USER,
        'PASSWORD': secrets.DB_LOGGER_PASSWORD,
        'HOST': secrets.DB_LOGGER_HOST,
        'PORT': secrets.DB_LOGGER_PORT,
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(pathname)s line %(lineno)d in %(funcName)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
        },
        'database': {
            'class': 'custom_db_logger.db_log_handler.DatabaseLogHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': config('DEFAULT_LOG_LEVEL', default='ERROR', cast=str),
        },
        'db_logger': {
            'handlers': ['database'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['database', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.*': {
            'handlers': ['database', 'mail_admins'],
            'propagate': True,
        },
        'proxies': {
            'handlers': ['database', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'throttling': {
            'handlers': ['database', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_THROTTLE_RATES': {
        'invalid_command': ['1/d'],
        'no_command': ['1/d'],
        'get_proxies': ['144/d'],
        'default': ['60/m'],
    },
    'NUM_PROXIES': config('NUM_PROXIES', default=None, cast=int),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

DOMAIN = config('DOMAIN')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ['GET', 'HEAD', 'OPTIONS']
CORS_URLS_REGEX = r'^/proxies/?$'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://' + config('REDIS_HOST') + ':6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': secrets.REDIS_PASSWORD
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
