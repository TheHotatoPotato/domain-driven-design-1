from flask import Flask, request
# import config
import model
import repository

app = Flask(__name__)
repo = repository.FakeToDoListRepository()

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/create-todo-list")
def create_todo_list():
    todo_list = model.ToDoList()
    repo.add(todo_list)
    return "Todo list created!"


if __name__ == "__main__":
    app.run(debug=True)