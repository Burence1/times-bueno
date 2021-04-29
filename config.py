import os

class Config:
  '''
  configurations parent class
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')


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