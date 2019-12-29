from main import create_app
from config import ProductionConfig

app = create_app(config=ProductionConfig)
