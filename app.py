from flask import Flask

from app.moduleUser.controller.user_controller import UserBlueprint
from app.moduleRoom.controller.room_controller import RoomBlueprint
from app.moduleRoom.model.rooms import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bolehmasuk@localhost:5432/db_test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(RoomBlueprint)
app.register_blueprint(UserBlueprint)

print("Registered Blueprints:", app.blueprints)
if __name__ == "__main__":
    app.run(debug=True)
