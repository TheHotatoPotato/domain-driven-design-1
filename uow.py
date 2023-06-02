import os
from abc import ABC, abstractmethod
import psycopg2

from repository import ToDoListAbstractRepository, ToDoListRepository


class AbstractUnitOfWork(ABC):
    todo_lists: ToDoListAbstractRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.commit()
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __enter__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='todo',
            user='moaz',
            password='',
            port=5432,
        )

        self.cursor = self.connection.cursor()

        self.todo_lists = ToDoListRepository(self.connection)

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
