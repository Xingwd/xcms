# -*- coding: UTF-8 -*-
from main import create_app, cli
from config import ProductionConfig

app = create_app(config=ProductionConfig)
cli.register(app)
