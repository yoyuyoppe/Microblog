import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'there-is-no-spoon'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://lewkis:123456@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
