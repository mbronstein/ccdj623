"""
Django settings for ccdj623 project.

Generated by 'django-admin startproject' using Django 4.0.5.

"""

from pathlib import Path
import environ
import django
from django.utils.encoding import smart_str

django.utils.encoding.smart_text = smart_str

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = ROOT_DIR / "ccd623"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", True)  # mb changed default to true
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(ROOT_DIR / ".env")

SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DEBUG = env.bool("DEBUG", True)
DEBUG_TOOLBAR = env.bool("DEBUG_TOOLBAR", True)
LOG_FILEPATH = env.str("LOG_FILEPATH", default=str(ROOT_DIR /"logs")
                       )
SILK = env.bool("SILK", False)

TIME_ZONE = 'America/New_York'
USE_TZ = True

SITE_ID = 1

LANGUAGE_CODE = "en-us"
USE_I18N = False
USE_L10N = False

LOCALE_PATHS = [str(ROOT_DIR / "locale")]

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ROOT_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {'default': env.db('DATABASE_URL')}

# caches : maybe have diff caches depending whether dev or prod?
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# URLS

ROOT_URLCONF = "ccdj623.urls"

WSGI_APPLICATION = "ccdj623.wsgi.application"

DJANGO_APPS = [
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    "django.forms",
    "grappelli",
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # "corsheaders",
    "django_comments_xtd",
    "django_comments",
    "taggit",
    "django_extensions",
    # "django_filters",
    "post_office",
    "django_mailbox",
    "reset_migrations",
    "model_utils",
    "import_export",
    "auditlog",
    "ckeditor",
    # "silk",
]

LOCAL_APPS = [
    "core.apps.CoreConfig",
    "matters.apps.MattersConfig",
    "events.apps.EventsConfig",
    "tasks.apps.TasksConfig",
    "entries.apps.EntriesConfig",
    "kbentries.apps.KbEntriesConfig",
    # "sops.apps.SopsConfig",
    "contacts.apps.AsContactConfig",
    # "apps.ssoffices.apps.SsofficesConfig"
    'timekeeping.apps.TimekeepingConfig'
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATION_MODULES = {"sites": "ccdj623.contrib.sites.migrations"}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'auditlog.middleware.AuditlogMiddleware',

]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [APPS_DIR / 'templates'],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (APPS_DIR / "fixtures")

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators


# EMAIL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

POST_OFFICE = {
    'DEFAULT_PRIORITY': 'now'
}
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=False)
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

PDFTK_PATH = env('PDFTK_PATH', default="")

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

# Static files (CSS, JavaScript, Images)


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(ROOT_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env.str("MEDIA_ROOT",
                     default=str(ROOT_DIR / "files")
                     )
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/files/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Mark Bronstein""", "mark@bronsteinlaw.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

TAGGIT_CASE_INSENSITIVE = True

# django-debug-toolbar
# ------------------------------------------------------------------------------
if DEBUG_TOOLBAR is True:
    INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
        "SHOW_TEMPLATE_CONTEXT": True,
    }

    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
    INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# DJANGO_AUDITLOG
AUDITLOG_INCLUDE_ALL_MODELS=True


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# if DEBUG is True:
if True:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s "
                          "%(process)d %(thread)d %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            }
        },
        "root": {"level": "INFO", "handlers": ["console"]},
    }
else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOG_FILEPATH,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

# AUTH_USER_MODEL = 'ccdj623.CustomUser'
# LOGIN_REDIRECT_URL = "home"
# LOGOUT_REDIRECT_URL = "home"
