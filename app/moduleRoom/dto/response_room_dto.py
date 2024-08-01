class RoomResponseDto:
    def serialize(self):
        return {"id": self.id, "name": self.name}
