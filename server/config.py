# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# https://dormousehole.readthedocs.io/en/latest/config.html#config
class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REGISTER_ENABLED = True


class ProductionConfig(Config):
    """Production Config"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'c39d2bf6ee0348aba82eb9bfd3c31e73')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'xcms.db'))
    REGISTER_ENABLED = False


class DevelopmentConfig(Config):
    """Development Config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'xcms.db')


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True
