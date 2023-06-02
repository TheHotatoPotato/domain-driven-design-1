from flask import Flask, request
# import config
from model import ToDoList, Item
from commands import create_todo, create_item, get_list
from uow import UnitOfWork
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/create-todo-list")
def create_todo_list():
    try:
        todolist = create_todo(uow=UnitOfWork())
        return_obj = {"message": "ToDoList created successfully!",
                      "todolist": todolist.to_do_id}
        return jsonify(return_obj), 201
    except Exception as e:
        return_obj = {"message": str(e)}
        return jsonify(return_obj), 500


@app.route("/get-todo-list", methods=["GET"])
def get_todo_list():
    try:
        todolist = get_list(uow=UnitOfWork())
        return_obj = {"message": "ToDoList retrieved successfully!",
                      "id": todolist.to_do_id, "type": str(type(todolist.to_do_id)), "items": todolist.items}
        return jsonify(return_obj), 200
    except Exception as e:
        print('here')
        return_obj = {"message": str(e)}
        return jsonify(return_obj), 500


@app.route("/create-item", methods=["POST"])
def create_item_route():
    try:
        data = request.get_json()
        title = data["title"]
        body = data["body"]
        completed = data["completed"]
        item = create_item(title=title, body=body,
                           completed=completed, uow=UnitOfWork())
        return_obj = {
            "message": "Item created successfully!", "id": item.item_id}
        return jsonify(return_obj), 201
    except Exception as e:
        return_obj = {"message": str(e)}
        return jsonify(return_obj), 500


if __name__ == "__main__":
    app.run(debug=True)
