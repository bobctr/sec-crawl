DOMAIN = {
    'news':{
        'schema':{
            '_id':{
                'type':'string',
            },
            'title':{
                'type':'string',
            },
            'author':{
                'type':'string',
            },
            'text':{
                'type':'string',            
            },
            'date':{
                'type':'string',            
            },
            'image':{
                'type':'string',            
            },
            'website':{
                'type':'string',            
            }
        }
    }
}
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'
# MONGO_AUTH_SOURCE = 'admin'  # needed if --auth mode is enabled

MONGO_DBNAME = 'sec-crawl'