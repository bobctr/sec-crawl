import os
from urllib.parse import quote_plus

X_DOMAINS = '*'
X_HEADERS = ['Authorization', 'Content-type']

DOMAIN = {
    'news': {
        'schema': {
            '_id': {
                'type': 'string',
            },
            'title': {
                'type': 'string',
            },
            'author': {
                'type': 'string',
            },
            'text': {
                'type': 'string',
            },
            'date': {
                'type': 'string',
            },
            'image': {
                'type': 'string',
            },
            'website': {
                'type': 'string',
            }
        }
    }
}

MONGO_USER = quote_plus(str(os.environ.get('MONGO_USER')))
MONGO_PSW = quote_plus(str(os.environ.get('MONGO_PSW'))) 
MONGO_HOSTNAME = quote_plus(str(os.environ.get('MONGO_HOSTNAME')))
MONGO_DBNAME = 'sec-crawl'
if((MONGO_USER, MONGO_PSW) is not (None, None)):
    MONGO_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_PSW}@{MONGO_HOSTNAME}/{MONGO_DBNAME}?retryWrites=true'
else:
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

