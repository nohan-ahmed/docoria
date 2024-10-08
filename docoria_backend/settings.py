"""
Django settings for docoria_backend project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import environ

# Initialize environ
env = environ.Env()
environ.Env.read_env()  # Load environment variables from .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6fx4^r-1(fsjy^@10_9=7m%+g*xzd^kl1!88k9l@3q)l_myacy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'accounts.User' # This allows using your custom user model for authentication 

# Application definition

INSTALLED_APPS = [
    # local apps
    'core',
    'accounts',
    'patients',
    'doctors',
    'education',
    'hospitals',
    'staffs',
    'services',
    'appointments',
    'notifications',
    'departments',
    'reviews',
    # third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'channels',
    'daphne',
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'docoria_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI_APPLICATION = 'docoria_backend.wsgi.application'
# Define ASGI application
ASGI_APPLICATION = 'docoria_backend.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Redis Channel Layer Configuration
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Django rest framework configuration.
REST_FRAMEWORK = {
    # JWT Configuration
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # apply the style globally, using the DEFAULT_PAGINATION_CLASS settings
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.StandardResultsSetPagination',
}

# You can customize JWT settings like token expiration times.
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    }

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
# Todo: Remove in production
STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# AWS S3 Configuration
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # Your AWS Access Key ID
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')  # Your AWS Secret Access Key
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')  # S3 Bucket Name
# AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', default='us-east-1')  # S3 Region
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # Custom S3 domain for accessing files
# AWS_DEFAULT_ACL = None  # Prevents S3 from applying default permissions to uploaded files (important for security)
# AWS_S3_FILE_OVERWRITE = False  # Prevent overwriting existing files with the same name
# AWS_QUERYSTRING_AUTH = False  # Disables query parameter authentication (good for public files)
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',  # Cache files for 24 hours to improve performance
#     'ContentDisposition': 'attachment',  # Forces downloads instead of inline display (optional, adjust as needed)
# }

# # Static and media files configuration
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # Using S3 for media file storage
#         "OPTIONS": {
#             "location": "media",  # Store media files in 'media' folder
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # Using S3 for static file storage
#         "OPTIONS": {
#             "location": "static",  # Store static files in 'static' folder
#         },
#     },
# }

# # Static and media URLs for serving files
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'  # URL to serve static files
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'  # URL to serve media files

# AWS S3 Configuration end.

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuring Email in Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')