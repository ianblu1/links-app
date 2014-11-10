class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False
    MONGOLAB_URI = 'mongodb://heroku_app31268112:amgre56nsqfmvkdk7berp0cas8@ds051170.mongolab.com:51170/heroku_app31268112'
    MONGODB_SETTINGS={'HOST': MONGOLAB_URI, 'DB': "links_app"}
#    SECRET_KEY = 'this-really-needs-to-be-changed'

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    MONGODB_SETTINGS={'DB': "links_app"}


class TestingConfig(Config):
    TESTING = True