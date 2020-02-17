from app import db


class User(db.Model):
    _table_=db.Model.metadata.tables['user']


class City(db.Model):
    _table_=db.Model.metadata.tables['city']


class Forecast(db.Model):
    _table_=db.Model.metadata.tables['forecast']