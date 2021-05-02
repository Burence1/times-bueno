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
  SQLALCHEMY_DATABASE_URI = "postgresql://zxfarvanyjjabm:0fa6bc00fdcf70bf2f60a91469d7fd3b297b3a328dff0065b5a2e8f2e92dd6b8@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d3m5ti8un7p46d?sslmode=require"

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
