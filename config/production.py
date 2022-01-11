from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='myprojectuser',
    pw='123123',
    url='localhost',
    db='myproject')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x9b\xfa\xc2\xb3\xf6\x024*_h\x00"\x8c2\x0f\xd6'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})