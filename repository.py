import abc
import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, ToDoList: model.ToDoList):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> model.ToDoList:
        raise NotImplementedError

class FakeToDoListRepository(AbstractRepository):
    def __init__(self):
        self.todo_lists: List[ToDoList] = []

    def add(self, todolist: model.ToDoList):
        if len(self.todo_lists) > 0:
            raise RepositoryException('Only one ToDoList allowed in the repository!')
        self.todo_lists.append(todolist)

    def get(self) -> model.ToDoList:
        return self.todo_lists[0]

    def save(self, todolist: model.ToDoList):
        self.todo_lists = []
        self.todo_lists.append(todolist)