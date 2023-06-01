import abc
from typing import List
# import psycopg2

from model import ToDoList, Item


class ToDoListAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, ToDoList: ToDoList):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> ToDoList:
        raise NotImplementedError

class FakeToDoListRepository(ToDoListAbstractRepository):
    def __init__(self):
        self.todo_lists: List[ToDoList] = []

    def add(self, todolist: ToDoList):
        # if len(self.todo_lists) > 0:
        #     raise RepositoryException('Only one ToDoList allowed in the repository!')
        self.todo_lists.append(todolist)

    def get(self) -> ToDoList:
        return self.todo_lists[0]

    def save(self, todolist: ToDoList):
        self.todo_lists = []
        self.todo_lists.append(todolist)

class ToDoListRepository(ToDoListAbstractRepository):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def add(self, todolist: ToDoList) -> None:
        self.cursor.execute(
            """
            INSERT INTO todolist (id) VALUES (%s)
            on conflict (id) do nothing;
            """,
            [todolist.to_do_id],
        )
        # for trying without uow
        # self.connection.commit()