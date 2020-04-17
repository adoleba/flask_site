import os


class Config:
    SECRET_KEY = 'x+9g6e8fz)ewi+t)3w5a5*96%(6a&_%z+@8(^xbu@fvih6bftj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    DEBUG = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'django.ania@gmail.com'
    MAIL_PASSWORD = '0987poiu'
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
