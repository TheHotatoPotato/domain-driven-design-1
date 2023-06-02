from dataclasses import dataclass, field
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

@dataclass
class Item:
    item_id: str
    title: str
    body: str
    completed: bool = False
    date_created: date = field(default_factory=date.today)

@dataclass(frozen=True)
class ToDoListHistory:
    date_created: date
    items: List[Item]

@dataclass
class ToDoList:
    to_do_id: str
    date_created: date = field(default_factory=date.today)
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        self.items.append(item)
        

    def edit_item(self, edited_item: Item):
        for item in self.items:
            if item.item_id == edited_item.id:
                item.title = edited_item.title
                item.body = edited_item.body

    def delete_item(self, to_delete_item: Item):
        self.items.remove(to_delete_item)

    def complete_item(self, to_complete_item: Item):
        for index, item in enumerate(self.items):
            if item.item_id == to_complete_item.item_id:
                self.items[index].completed = True