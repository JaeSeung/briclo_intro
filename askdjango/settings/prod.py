from .common import *

DEBUG = False  # 개발모드 여부
ALLOWED_HOSTS = ['*']

STATIC_ROOT  = os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ubuntu',
        'USER': 'ubuntu',
        'PASSWORD': 'withaskdjango!',
        'HOST': '127.0.0.1',
    },
}
