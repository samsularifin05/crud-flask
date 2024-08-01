from app.moduleRoom.model.rooms import Room

class RoomRepository:
    def get_all_rooms(self, session):
        return session.query(Room).all()

    def create(self, session, name):
        new_room = Room(name=name)
        session.add(new_room)
        session.commit()
        return new_room