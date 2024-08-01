from app.moduleRoom.repository.room_repository import RoomRepository
from flask import current_app
from app.moduleRoom.dto.request_room_dto import RoomCreateRequestDto
from app.moduleRoom.model.rooms import db

def get_session():
    return db.session

def fetch_all_rooms():
    session = get_session() 
    try:
        repo = RoomRepository()
        return repo.get_all_rooms(session)
    finally:
        session.remove()  

def add_new_room(body: RoomCreateRequestDto):
    session = get_session()
    try:
        name = body.name
        repo = RoomRepository()
        return repo.create(session, name)
    finally:
        session.remove() 