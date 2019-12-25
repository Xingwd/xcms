# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB = os.environ.get('MONGO_DB', 'xcms')

    # Blog
    BLOG_LIMIT = int(os.environ.get('BLOG_LIMIT', 5))


class ProductionConfig(Config):
    """Production Config"""
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))


class DevelopmentConfig(Config):
    """Development Config"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True
