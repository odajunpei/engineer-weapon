"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
# 追加
import os
# from .environ import DEBUG
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# #追加
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j1kwd_o_a=hubuwmh)1e*5%h!jv&9_a&m00fq&0g#g37+0_#q*'
# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'article',
    'studytime',
    'markdownx',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    # DRF
    'django_cleanup.apps.CleanupConfig',  # django-cleanupを使いたいなら、これも追加
    'rest_framework',
    'storages',
    # 'axes',
    'django_filters',
]

AUTHENTICATION_BACKENDS = [
    # 'axes.backends.AxesBackend',  # 認証に使用するのでここにも追加。必ず先頭に。
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'base', ],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DEBUG = int(os.environ.get('DEBUG', default=0))

if DEBUG:
    ALLOWED_HOSTS = ['*']

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': str(BASE_DIR / 'db.sqlite3'),
    #     }
    # }
else:
    ALLOWED_HOSTS = ['49.212.153.160']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myproject',
            'USER': 'myprojectuser2',
            'PASSWORD': 'password',
            'HOST': '49.212.153.160',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '#kadfG834f+-sa',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, "assets")),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# カスタムユーザーを使う
AUTH_USER_MODEL = 'accounts.User'

# ログインページと、直接ログインページへ行った後のリダイレクトページ
LOGIN_URL = 'accounts/login'
LOGIN_REDIRECT_URL = '../../accounts/profile'
LOGOUT_REDIRECT_URL = "/"
# メールをコンソールに表示する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FILE_UPLOAD_PERMISSIONS = 0o644

# 大きいサイズの場合
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 * 1000  # 2.5M×10=2500M

MARKDOWNX_IMAGE_MAX_SIZE = {'size': (1000, 1000), 'quality': 100}

custom_file_limit = 2621440 * 10  # 25Mまで
SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': custom_file_limit,  # specify the file size
}
SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTIONS = "SAMEORIGIN"
SITE_ID = 1

INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

DEBUG = int(os.environ.get('DEBUG', default=0))
if DEBUG:
    CORS_ORIGIN_WHITELIST = (
        'http://127.0.0.1:8080',
        'http://localhost:8080',
    )
else:
    CORS_ORIGIN_WHITELIST = (
        'https://tryad-portal-s3.s3.amazonaws.com',
    )

# キャッシュの設定。django.core.cache.backends.locmem.LocMemCache を使っている場合は設定
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    # 'axes_cache': {
    #     'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    # }
}
# AXES_CACHE = 'axes'
# AXES_FAILURE_LIMIT = 15  # ログイン失敗10回まで
# AXES_COOLOFF_TIME = 24  # ログインを連続で失敗した場合は24時間アカウントがロック

# AXES_META_PRECEDENCE_ORDER = (
#     'HTTP_X_FORWARDED_FOR',
# )

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

# 本番環境はS3で配信
# if not DEBUG:
#     # 共通の設定
#     AWS_ACCESS_KEY_ID = 'AKIA5EA3TRWW4MPE5T7V'
#     AWS_SECRET_ACCESS_KEY = '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'
#     AWS_STORAGE_BUCKET_NAME = 'tryad-portal-s3'
#     AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#     AWS_S3_OBJECT_PARAMETERS = {
#         'CacheControl': 'max-age=86400',  # 1日はそのキャッシュを使う
#     }

#     # 静的ファイルの設定
#     AWS_LOCATION = 'static'
#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#     # djangoからの保存を基本、パブリック公開にする
#     AWS_DEFAULT_ACL = 'public-read'

#     # メディアファイルの設定。今回は「project」というプロジェクト名の例
#     DEFAULT_FILE_STORAGE = 'project.backends.MediaStorage'

    # 本番はsentry使う
    # import sentry_sdk
    # from sentry_sdk.integrations.django import DjangoIntegration

    # sentry_sdk.init(
    #     dsn="https://861304876725473aaa551c6d6c6cb050@o486824.ingest.sentry.io/5631086",
    #     integrations=[DjangoIntegration()],
    #     traces_sample_rate=1.0,

    #     # If you wish to associate users to errors (assuming you are using
    #     # django.contrib.auth) you may enable sending PII data.
    #     send_default_pii=True
    # )