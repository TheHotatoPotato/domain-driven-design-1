import model
import repository

def test_repository_can_add_a_todo_list():
    repo = repository.FakeToDoListRepository()
    todo_list = model.ToDoList()
    repo.add(todo_list)
    assert repo.get() == todo_list

def test_repository_can_save_a_todo_list():
    repo = repository.FakeToDoListRepository()
    todo_list = model.ToDoList()
    repo.add(todo_list)
    todo_list.add_item(model.Item('Test', 'Test'))
    repo.save(todo_list)
    assert repo.get() == todo_list