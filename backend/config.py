# import os

# class Config:
#     """Base configuration with default settings."""
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Use environment variable or default
#     DEBUG = False

# class DevelopmentConfig(Config):
#     """Development environment settings."""
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "sqlite:///DelishDine.db"

# class ProductionConfig(Config):
#     """Production environment settings."""
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///DelishDine.db")  # Use a real database in production

# # Dictionary to select the config
# config_dict = {
#     "development": DevelopmentConfig,
#     "production": ProductionConfig,
# }


import os

class Config:
    """Base configuration with default settings."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Use environment variable or default
    DEBUG = False

class DevelopmentConfig(Config):
    """Development environment settings."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///DelishDine.db"

class ProductionConfig(Config):
    """Production environment settings."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///DelishDine.db")  # Use a real database in production

# Dictionary to select the config
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
