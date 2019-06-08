# -*- coding: UTF-8 -*-
from flask import Flask
from conf.config import ProductionConfig, DevelopmentConfig


def create_app(Config=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(Config)

    return app


if __name__ == '__main__':
    app = create_app(config=DevelopmentConfig)
    app.run(host='0.0.0.0')
