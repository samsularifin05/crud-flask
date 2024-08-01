from flask import Blueprint, jsonify, request, abort
from flask_openapi3 import Tag, APIBlueprint
from app.moduleRoom.service.room_service import fetch_all_rooms, add_new_room
from utils.base_respons import BaseResponse
from app.moduleRoom.dto.request_room_dto import RoomCreateRequestDto
from app.moduleRoom.dto.response_room_dto import RoomResponseDto


tag = Tag(name="Room", description="RoomController")
RoomBlueprint = APIBlueprint(
    "/room", __name__, url_prefix="/api/room", abp_tags=[tag]
)

@RoomBlueprint.get('')
def show_rooms():
    data = fetch_all_rooms()
    return BaseResponse.serialize_list(
        200,
        "Get all success",
        [RoomResponseDto.serialize(item) for item in data],
    )

@RoomBlueprint.post('')
def add_room(body: RoomCreateRequestDto):
    add_new_room(body)
    return BaseResponse.serialize_object(
        200, "Creat success", []
    )