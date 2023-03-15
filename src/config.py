import os

# Configuration class for Flask app
class Config(object):
    # Disable SQLAlchemy modification tracking 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Get the value of SECRET_KEY from environment variable
    JWT_SECRET_KEY =  os.environ.get("SECRET_KEY")
    # Disable sorting of JSON keys 
    JSON_SORT_KEYS = False
    # Get the database URI from environment variable
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Access to .env and get the value of DATABASE_URL
        value = os.environ.get("DATABASE_URL")
        # Raise an error if the database URI is not set
        if not value:
            raise ValueError("DATABASE_URL is not set")
        return value

# Development configuration class
class DevelopmentConfig(Config):
    DEBUG = True
# Production configuration class
class ProductionConfig(Config):
    pass
# Testing configuration class
class TestingConfig(Config):
    TESTING = True

# Get the Flask environment mode from environment variable
environment = os.environ.get("FLASK_ENV")

# Set the app configuration based on the environment mode
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()