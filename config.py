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
  SQLALCHEMY_DATABASE_URI = "postgresql://yvcdjrrkthyxib:b1b160e9b35c5f7bd30bf57019c41b6ad217723e19345308753dcc1dbb6a31e0@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d9sjsj062k7jpa?sslmode=require"

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
