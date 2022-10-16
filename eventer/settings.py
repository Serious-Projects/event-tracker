import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Setting environment configurations
env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e0f=x%43*4ge9yuzluej&cy(-wgih=wl3b(ali5nv!*0a)cm2y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
   '127.0.0.1',
   'eventer.up.railway.app',
]

# Admin User Model
AUTH_USER_MODEL = 'base.User'

# Application definition
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'corsheaders',
   'widget_tweaks',
   'base',
]

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'whitenoise.middleware.WhiteNoiseMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'corsheaders.middleware.CorsMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventer.urls'

TEMPLATES = [
   {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'eventer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# Postgesql Database Configuration (production)
DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': env('PGDATABASE'),
      'USER': env('PGUSER'),
      'PASSWORD': env('PGPASSWORD'),
      'HOST': env('PGHOST'),
      'PORT': env('PGPORT'),
   }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
   BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
   'http://127.0.0.1:8000',
   'https://web-production-9860.up.railway.app',
   'https://eventer.up.railway.app',
]