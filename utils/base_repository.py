from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self, session: Session):
        return session.query(self.model).all()

    def get_by_id(self, session: Session, id: int):
        return session.query(self.model).get(id)

    def find_one(self, session: Session, **kwargs):
        try:
            return session.query(self.model).filter_by(**kwargs).one()
        except NoResultFound:
            return None

    def find_by(self, session: Session, **kwargs):
        return session.query(self.model).filter_by(**kwargs).all()
