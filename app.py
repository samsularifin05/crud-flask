from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.moduleUser.controller.user_controller import UserBlueprint
from app.moduleRoom.controller.room_controller import RoomBlueprint
from app.moduleRoom.model.rooms import db

app = Flask(__name__)

# Replace the database URI with your SQL Server connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SA:Bolehmasuk123@localhost/CRUD?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(RoomBlueprint)
app.register_blueprint(UserBlueprint)

print("Registered Blueprints:", app.blueprints)
if __name__ == "__main__":
    app.run(debug=True)
