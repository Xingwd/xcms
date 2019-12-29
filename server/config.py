# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# TODO: 学习flask配置，https://dormousehole.readthedocs.io/en/latest/config.html#config
class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production Config"""
    @property
    def SECRET_KEY(self):
        value = os.environ.get('SECRET_KEY')
        if value:
            return value
        else:
            raise ValueError("No SECRET_KEY set for Flask application")

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if value:
            return value
        else:
            raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application")


class DevelopmentConfig(Config):
    """Development Config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'xcms.db')


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True
