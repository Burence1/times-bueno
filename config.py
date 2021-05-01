import os

class Config:
  '''
  configurations parent class
  '''
  QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'


  @staticmethod
  def init_app(app):
    pass

class ProdConfig(Config):
  '''
  production configurations, child class
  '''
  pass

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
