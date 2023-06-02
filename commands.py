from model import ToDoList, Item
from uow import AbstractUnitOfWork
from datetime import date
from uuid import uuid4

def create_todo(uow: AbstractUnitOfWork) -> ToDoList:
    todolist = ToDoList(to_do_id=str(uuid4()), date_created=date.today())
    with uow:
        uow.todo_lists.add(todolist)
        uow.commit()

    return todolist

def get_list(uow: AbstractUnitOfWork) -> ToDoList:
    with uow:
        todolist = uow.todo_lists.get()
    return todolist

# id, todolist_id, title, body, completed, date_created
def create_item(title: str, body: str, completed: bool, uow: AbstractUnitOfWork) -> Item:
    item = Item(item_id=str(uuid4()), title=title, body=body, completed=completed, date_created=date.today())
    with uow:
        todolist = uow.todo_lists.get()
        todolist.add_item(item)
        uow.todo_lists.save(todolist)
        uow.commit()
    return item