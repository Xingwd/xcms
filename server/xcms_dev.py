# -*- coding: UTF-8 -*-
from main import create_app
from config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)
