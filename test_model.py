from datetime import date, timedelta
import pytest
from model import Item, ToDoList

def test_adding_item_increments_list():
    todo_list = ToDoList()
    todo_list.add_item(Item('Test', 'Test'))
    assert len(todo_list.get_items) == 1

def test_editing_item_changes_item():
    todo_list = ToDoList()
    item = Item('Test', 'Test')
    todo_list.add_item(item)
    todo_list.edit_item(item, Item('Test 2', 'Test 2'))
    assert todo_list.get_items[0].title == 'Test 2'

def test_deleting_item_decrements_list():
    todo_list = ToDoList()
    item = Item('Test', 'Test')
    todo_list.add_item(item)
    todo_list.delete_item(item)
    assert len(todo_list.get_items) == 0

def test_completing_item_marks_item_completed():
    todo_list = ToDoList()
    item = Item('Test', 'Test')
    todo_list.add_item(item)
    todo_list.complete_item(item)
    print(todo_list.get_items[0].completed)
    assert todo_list.get_items[0].completed == True

def test_reordering_item_changes_item_index():
    todo_list = ToDoList()
    item = Item('Test', 'Test')
    todo_list.add_item(item)
    todo_list.add_item(Item('Test 2', 'Test 2'))
    todo_list.reorder_item(item, 1)
    assert todo_list.get_items[1] == item