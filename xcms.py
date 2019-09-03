from server import create_app
from conf.config import ProductionConfig, DevelopmentConfig


app = create_app(ProductionConfig)


if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    app.run(host='0.0.0.0', debug=True)
