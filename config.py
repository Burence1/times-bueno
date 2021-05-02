import os

class Config:
  '''
  configurations parent class
  '''
  QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


  @staticmethod
  def init_app(app):
    pass

class ProdConfig(Config):
  '''
  production configurations, child class
  '''
  SQLALCHEMY_DATABASE_URI = "postgresql://kotwyrvtsjowoe:4893265466602ff386ce52b9eaa7b9fcb66a7a1238ce687da2361c2507a31404@ec2-52-21-153-207.compute-1.amazonaws.com:5432/dema08htipugr9?sslmode=require"

class DevConfig(Config):
  '''
  development configurations, child class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://burens:Hawaii@localhost/times'

  DEBUG=True

config_options={
  'development':DevConfig,
  'production':ProdConfig
}
