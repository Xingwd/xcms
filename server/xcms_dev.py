# -*- coding: UTF-8 -*-
from main import create_app, cli
from config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)
cli.register(app)
