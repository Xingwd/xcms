from server.main import create_app
from conf.config import ProductionConfig, DevelopmentConfig


app = create_app(config=ProductionConfig)


if __name__ == '__main__':
    app = create_app(config=DevelopmentConfig)
    app.run(host='0.0.0.0', debug=True)
