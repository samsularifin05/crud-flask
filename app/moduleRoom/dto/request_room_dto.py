from pydantic import BaseModel

class RoomCreateRequestDto(BaseModel):
    name: str
class RoomGetByIdRequest(BaseModel):
    id: int
    

