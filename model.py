from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

'''
Use Cases / Requirements:
- Multiple users
- Users can access their own todo lists
- Users can add tasks to their todo list
- Users can mark tasks as completed
- Users can edit a task
- Users can delete a task
- Users can reorder their tasks
- Users can view the history of their todo list for any given day
'''

@dataclass(frozen=True)
class Item:
    title: str
    body: str
    completed: bool = False
    day_added: date = date.today()

class List:
    def __init__(self, user: str):
        self.user = user
        self.items = []

    def __repr__(self):
        return f"<List {self.user}>"

    def add_item(self, item: Item):
        self.items.append(item)

    def edit_item(self, item: Item, new_item: Item):
        self.items[self.items.index(item)] = new_item

    def delete_item(self, item: Item):
        self.items.remove(item)

    def complete_item(self, item: Item):
        item.completed = True

    def reorder_item(self, item: Item, new_index: int):
        self.items.remove(item)
        self.items.insert(new_index, item)

    @property
    def get_history(self, date: date):
        return [item for item in self.items if item.day_added == date]

    @property
    def get_items(self):
        return self.items

    @property
    def get_user(self):
        return self.user