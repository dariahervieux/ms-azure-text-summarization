"""Flask configuration file
  inspired by https://hackingandslacking.com/configuring-your-flask-application-4e5341d7affb
""" 
class Config:
    """Set Flask config variables."""
    DEBUG = True
    FLASK_ENV = 'development'
    UPLOAD_FOLDER = 'static/tmp/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

