import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("MAP_GEN_SECRET_KEY") or "test key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("MAP_GEN_DEV_DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("MAP_GEN_TEST_DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "data-test.sqlite")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("MAP_GEN_DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "data.sqlite")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}