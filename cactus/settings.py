import os

import djcelery
from logz import log

djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#1r8yj1!ch(9z=qg-chkwyvt_i^7tx12(*89!xcu8xz9hl(*wi'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'rest_framework',

    'api_test'
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

ROOT_URLCONF = 'cactus.urls'

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

WSGI_APPLICATION = 'cactus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_L10N = False

USE_I18N = True

USE_TZ = True

DATETIME_FORMAT = 'Y年m月d日 H:i:s'

DATE_FORMAT = 'Y年m月d日'


STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True  # 是否使用SSL加密
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'rpa@secoo.com'
EMAIL_HOST_PASSWORD = 'Youxiang_00137'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}


BROKER_URL = 'redis://10.0.254.121:6379/10'
# BROKER_TRANSPORT = 'redis'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERYD_MAX_TASKS_PER_CHILD = 100
CELERYD_CONCURRENCY = 20
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_IMPORTS = ('crontab.task', )
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'#定时任务调度 配置存储到数据库 所以可以web端动态添加哦
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend' # 结果存储，我配置的是存储到数据库
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CELERY_DEFAULT_QUEUE = 'default'

# CELERY_QUEUES = {
#     "default": {"exchange": "default", "exchange_type": "direct", "routing_key": "default"},
#     "topicqueue": {"exchange": "topic", "exchange_type": "topic", "routing_key": "topictest.#"},
# }