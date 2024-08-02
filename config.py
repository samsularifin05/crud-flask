import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://SA:Bolehmasuk123@localhost/CRUD?driver=ODBC+Driver+17+for+SQL+Server"
