from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
