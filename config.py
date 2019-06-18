import os

class Config():
    GPAAS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(GPAAS_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(GPAAS_DIR, 'media')
