"""
might not need this file
"""

# from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import mapper, relationship

# import model

# metadata = MetaData()

# items = Table(
#     'items', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('title', String(255), nullable=False),
#     Column('body', String(255), nullable=False),
#     Column('completed', Integer, nullable=False),
#     Column('day_added', Date, nullable=False)
# )

# # to do list table
# todo_list = Table(
#     'todo_list', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('item_id', Integer, ForeignKey('items.id'))
# )

# # mapper
# def start_mappers():
#     mapper(model.Item, items, properties={
#         '_id': items.c.id,
#         '_title': items.c.title,
#         '_body': items.c.body,
#         '_completed': items.c.completed,
#         '_day_added': items.c.day_added
#     })

#     mapper(model.ToDoList, todo_list, properties={
#         '_id': todo_list.c.id,
#         '_user_id': todo_list.c.user_id,
#         '_item_id': todo_list.c.item_id
#     })