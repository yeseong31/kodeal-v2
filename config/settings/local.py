import dj_database_url
import openai

from . import my_settings

openai.api_key = my_settings.OPENAI_CODEX_KEY
openai.Engine.list()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = my_settings.DATABASES

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Email Authentication
EMAIL_BACKEND = my_settings.EMAIL['EMAIL_BACKEND']
EMAIL_USE_TLS = my_settings.EMAIL['EMAIL_USE_TLS']
EMAIL_PORT = my_settings.EMAIL['EMAIL_PORT']
EMAIL_HOST = my_settings.EMAIL['EMAIL_HOST']
EMAIL_HOST_USER = my_settings.EMAIL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = my_settings.EMAIL['EMAIL_HOST_PASSWORD']
SERVER_EMAIL = my_settings.EMAIL['SERVER_EMAIL']

# Generate JWT Token
JWT_SECRET_KEY = my_settings.JWT_SECRET_KEY

# Naver Papago
CLIENT_ID = my_settings.CLIENT_ID
CLIENT_SECRET = my_settings.CLIENT_SECRET
