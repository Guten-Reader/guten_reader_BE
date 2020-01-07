class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    ENV = 'production'


class StagingConfig(Config):
    ENV = 'staging'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    ENV = 'test'
    TESTING = True
