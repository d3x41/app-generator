"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os, random, string, json
from pathlib import Path
from django.contrib import messages
from str2bool import str2bool 
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = '426967205465636820436F6D70616E69657320616E6420564373204B696C6C20476F6F64204C6966650A'

PRO_SUBSCRIPTION_PRICE = os.environ.get('PRO_SUBSCRIPTION_PRICE', '4.99')
PRO_SUBSCRIPTION_COMPANY_PRICE = os.environ.get('PRO_SUBSCRIPTION_COMPANY_PRICE', '39')
CUST_DEV_WEEK_PRICE  = '1499' #os.environ.get('CUST_DEV_WEEK_PRICE', '899')
CUST_DEV_HOUR_PRICE  = '39' #os.environ.get('CUST_DEV_HOUR_PRICE', '29')
ONBOARDING_KIT_PRICE = '99' #os.environ.get('ONBOARDING_KIT_PRICE', '49')
BUNDLE_PRICE  = '149' #os.environ.get('BUNDLE_PRICE', '149')

# Enable/Disable DEBUG Mode
DEBUG = str2bool(os.environ.get('DEBUG'))

# Hosts Settings
ALLOWED_HOSTS = [ 'localhost', '127.0.0.1', '81.181.87.190', '0.0.0.0', 'app-generator.dev', 'development.app-generator.dev' ]
CSRF_TRUSTED_ORIGINS = [ 'http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://127.0.0.1:5085', 'https://app-generator.dev', 'http://app-generator.dev', 'http://development.app-generator.dev', 'https://development.app-generator.dev']

# Application definition

INSTALLED_APPS = [
    "webpack_loader",
    "frontend",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # CLI
    "cli",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
    "django_filters",
    "corsheaders",

    # APPS
    "apps.ai_processor",
    "apps.api",
    "apps.common",
    "apps.pages",
    "apps.authentication",
    "apps.blog",
    "apps.dashboard",

    "apps.products",
    "apps.tasks",
    "apps.support",

    "apps.tools",
    "apps.tool_db_migrator",
    "apps.tool_django_generator",
    "apps.tool_flask_generator",

    # Util
    "docs",
    "sslserver",

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'django_quill',
    'django_celery_results',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Util
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # allauth 
    "allauth.account.middleware.AccountMiddleware",

    # Custom
    "apps.dashboard.log_middleware.APILoggingMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "core.urls"

UI_TEMPLATES = os.path.join(BASE_DIR, 'templates') 

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [UI_TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                "apps.common.context_processors.profile_context",
                "apps.common.context_processors.version_context",
                "apps.common.context_processors.props_context",
                "apps.common.context_processors.google_tag",

                "apps.common.context_processors.price_subscription_pro",
                "apps.common.context_processors.price_subscription_company",
                "apps.common.context_processors.price_cust_dev_week",
                "apps.common.context_processors.price_cust_dev_hour",
                "apps.common.context_processors.price_onboarding_kit",
                "apps.common.context_processors.price_bundle",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DB_ENGINE   = os.environ.get('DB_ENGINE')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASS     = os.environ.get('DB_PASS')
DB_HOST     = os.environ.get('DB_HOST')
DB_PORT     = os.environ.get('DB_PORT')
DB_NAME     = os.environ.get('DB_NAME')

if DB_ENGINE and DB_NAME and DB_USERNAME:
    DATABASES = { 
        'default': {
            'ENGINE'  : 'django.db.backends.' + DB_ENGINE, 
            'NAME'    : DB_NAME,
            'USER'    : DB_USERNAME,
            'PASSWORD': DB_PASS,
            'HOST'    : DB_HOST,
            'PORT'    : DB_PORT,
        },          
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME'  : 'db.sqlite3',
        },
        # 'db_src': {
        #     'ENGINE'  : 'django.db.backends.'  + os.environ.get('DB_SRC_ENGINE', 'NOT_SET'), 
        #     'NAME'    : os.environ.get('DB_SRC_NAME' , None),
        #     'USER'    : os.environ.get('DB_SRC_USERNAME', None),
        #     'PASSWORD': os.environ.get('DB_SRC_PASS', None),
        #     'HOST'    : os.environ.get('DB_SRC_HOST', None),
        #     'PORT'    : os.environ.get('DB_SRC_PORT', None),
        # },
        # 'db_dest': {
        #     'ENGINE'  : 'django.db.backends.'  + os.environ.get('DB_DEST_ENGINE', 'NOT_SET'), 
        #     'NAME'    : os.environ.get('DB_DEST_NAME' , None),
        #     'USER'    : os.environ.get('DB_DEST_USERNAME', None),
        #     'PASSWORD': os.environ.get('DB_DEST_PASS', None),
        #     'HOST'    : os.environ.get('DB_DEST_HOST', None),
        #     'PORT'    : os.environ.get('DB_DEST_PORT', None),
        # },
    } 


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.INFO: 'text-blue-800 border border-blue-300 bg-blue-50 dark:text-blue-400 dark:border-blue-800',
    messages.SUCCESS: 'text-green-800 border border-green-300 bg-green-50 dark:text-green-400 dark:border-green-800',
    messages.WARNING: 'text-yellow-800 border border-yellow-300 bg-yellow-50 dark:text-yellow-300 dark:border-yellow-800',
    messages.ERROR: 'text-red-800 border border-red-300 bg-red-50 dark:text-red-400 dark:border-red-800',
}

SITE_ID = 1
LOGIN_REDIRECT_URL = "/dashboard/profile/"

# OAuth
GITHUB_CLIENT_ID   = os.getenv("GITHUB_CLIENT_ID" , "")
GITHUB_SECRET_KEY  = os.getenv("GITHUB_SECRET_KEY", "") 

# Upload 
GITHUB_API_KEY     = os.getenv("GITHUB_API_KEY", None) 
GITHUB_API_ACCOUNT = os.getenv("GITHUB_API_ACCOUNT", 'https://github.com/appseed-projects4/') 

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'read:user',
            'user:email'
        ],        
        "APP": {
            "client_id": GITHUB_CLIENT_ID,
            "secret": GITHUB_SECRET_KEY,
        },
    },
}

SOCIALACCOUNT_QUERY_EMAIL = True

QUILL_CONFIGS = {
    'default':{
      "theme": "snow",
      "modules": {
        "syntax": True,
        "toolbar": [
          [
            {"header": []},
            {"align": []},
            "bold",
            "italic",
            "underline",
            "strike",
            "blockquote",
          ],
          ["code-block", "link"],
        ],
        "imageCompressor": {
          "quality": 0.8,
          "maxWidth": 2000,
          "maxHeight": 2000,
          "imageType": "image/jpeg",
          "debug": False,
          "suppressErrorLogging": True
        },
        "resize": {
          "showSize": True,
          "locale": {}
        }
      },
      "formats": [
        "header",
        "bold",
        "italic",
        "underline",
        "strike",
        "blockquote",
        "code-block",
        "link",
        "indent",
        "list",
        "align",
      ],
      "sanitize": True,
    }
}

# ### Async Tasks (Celery) Settings ###

CELERY_SCRIPTS_DIR        = os.path.join(BASE_DIR, "tasks_scripts" )

# CELERY_LOGS_URL           = "/tasks_logs/"
# CELERY_LOGS_DIR           = os.path.join(BASE_DIR, "tasks_logs"    )

CELERY_BROKER_URL         = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND     = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT    = 30 * 60
CELERY_CACHE_BACKEND      = "django-cache"
CELERY_RESULT_BACKEND     = "django-db"
CELERY_RESULT_EXTENDED    = True
CELERY_RESULT_EXPIRES     = 60*60*24*30 # Results expire after 1 month
CELERY_ACCEPT_CONTENT     = ["json"]
CELERY_TASK_SERIALIZER    = 'json'
CELERY_RESULT_SERIALIZER  = 'json'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
########################################


# DOCS_ROOT = os.path.join(BASE_DIR, 'docs/build/html')

DOCS_ROOT = os.path.join(BASE_DIR, 'docs/build/html')
DOCS_ACCESS = 'public'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_PORT=465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_DISPLAY_NAME=os.environ.get('EMAIL_DISPLAY_NAME')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    #'DEFAULT_THROTTLE_CLASSES': [
    #    'apps.api.throttling.OncePerMinuteThrottle',
    #],
    #'DEFAULT_THROTTLE_RATES': {
    #    'once_per_minute': '1/min',
    #},
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

GUMROAD_ACCESS_TOKEN = os.environ.get('GUMROAD_ACCESS_TOKEN')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "frontend/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
    }
} 

VERSION = open('VERSION', 'r').readline()

LIMIT_AI_PROMPT_GUEST = os.environ.get('LIMIT_AI_PROMPT_GUEST', 3)
LIMIT_AI_PROMPT_AUTH  = os.environ.get('LIMIT_AI_PROMPT_AUTH' , 5)

# Redirects file
REDIRECTS_PATH = os.path.join('templates', 'redirects.json')
REDIRECTS = json.loads( open( REDIRECTS_PATH, 'r').read() )

# Limits
CSV_PROCESS_LIMIT = os.environ.get('CSV_PROCESS_LIMIT', 20)
X_FRAME_OPTIONS = 'SAMEORIGIN'

# 
GOOGLE_TAG = os.environ.get('GOOGLE_TAG', None)