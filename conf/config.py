# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB = 'xcms'


class ProductionConfig(Config):
    """Production Config"""
    MONGO_HOST = os.environ.get('MONGO_HOST') or 'localhost'
    MONGO_PORT = os.environ.get('MONGO_PORT') or 27017
    MONGO_DB = os.environ.get('MONGO_DB') or 'xcms'


class DevelopmentConfig(Config):
    """Development Config"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True
