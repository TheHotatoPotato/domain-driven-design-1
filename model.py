from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

'''
Use Cases / Requirements:
- Single user
- User can add tasks to their todo list
- User can mark tasks as completed
- User can edit a task
- User can delete a task
- User can reorder their tasks
- User can view the history of their todo list for any given day
'''

@dataclass()
class Item:
    title: str
    body: str
    completed: bool = False
    day_added: date = date.today()

class List:
    def __init__(self):
        self.items: List[Item] = []

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