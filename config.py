class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI = "postgresql://apierce:password@localhost/hello_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
