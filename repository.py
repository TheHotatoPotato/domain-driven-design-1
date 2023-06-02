import abc
from typing import List
# import psycopg2

from model import ToDoList, Item

class ToDoListAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, todolist: ToDoList):
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

    def get(self) -> ToDoList:
        self.cursor.execute(
            """
            SELECT * FROM todolist
            """
        )
        result = self.cursor.fetchone()
        todolist = ToDoList(to_do_id=result[0], date_created=result[1])

        sql = """
            SELECT id, todolist_id, title, body, completed, date_created from items where todolist_id = %s
        """
        self.cursor.execute(sql, [todolist.to_do_id])
        rows = self.cursor.fetchall()
        todolist.items = [Item(item_id=item[0], title=item[2], body=item[3], completed=item[4], date_created=item[5]) for item in rows]
        
        return todolist

    def save(self, todolist: ToDoList) -> None:
        print('there')
        print(todolist.to_do_id)
        self.cursor.execute(
            """
            DELETE FROM items where todolist_id = %s
            """,
            [todolist.to_do_id]
        )
        sql = """
            INSERT INTO items (id, todolist_id, title, body, completed, date_created) values
        """
        args = [(item.item_id, todolist.to_do_id, item.title, item.body, item.completed, item.date_created) for item in todolist.items]
        args_str = ','.join(self.cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x).decode("utf-8") for x in args)
        self.cursor.execute(sql + (args_str))