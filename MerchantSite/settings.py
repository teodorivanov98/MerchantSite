import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-dev-key')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'merchantsite.onrender.com',
    'teodor-ivanov.onrender.com',
]

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'products',
    'cart',
    'orders',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL CONFIG
ROOT_URLCONF = 'MerchantSite.urls'

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

WSGI_APPLICATION = 'MerchantSite.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Dev static files
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Collected static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# LOGIN / LOGOUT
LOGIN_REDIRECT_URL = 'product_list'
LOGOUT_REDIRECT_URL = 'login'

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER', 'your_gmail_address@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS', 'your_gmail_app_password')
DEFAULT_FROM_EMAIL = f'BeverageMerchant <{EMAIL_HOST_USER}>'
PASSWORD_RESET_EMAIL_TEMPLATE_NAME = 'registration/password_reset_email.html'\

# AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
