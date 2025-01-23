# The Repository pattern is an abstraction over persistent storage
import abc
from typing import List

from sqlmodel import Session
from src.allocation.domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.BatchModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.BatchModel:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[model.BatchModel]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get(self, reference: int) -> model.BatchModel:
        return self.session.query(model.BatchModel).filter_by(reference=reference).one()

    def add(self, batch: model.BatchModel) -> None:
        self.session.add(batch)

    def list(self) -> List[model.BatchModel]:
        return self.session.query(model.BatchModel).all()
