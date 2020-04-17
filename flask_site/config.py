import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    DEBUG = False
    POSTS_PER_PAGE = 6


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql:///flask"
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    "development": "flask_site.config.DevelopmentConfig",
    "testing": "flask_site.config.TestingConfig",
    "production": "flask_site.config.ProductionConfig",
}
