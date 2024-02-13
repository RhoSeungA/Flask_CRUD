from api.database import db
from api.models.todo import Todo
from api.services.user_service import get_user_by_id
from api.errors import InvalidTitleError, InvalidContentError, TodoNotExistError

def get_todo_by_user_id(id):
    user = get_user_by_id(id)
    return Todo.query.filter_by(user=user).all()
def get_todo_by_todo_id(id):
    return Todo.query.filter_by(id=id).first()

def get_all_todo():
    return Todo.query.all()

def add_todo(user,title, content):
    if not title:
        raise InvalidTitleError
    if not content:
        raise InvalidContentError

    todo = Todo(user=user,title=title, content=content)

    db.session.add(todo)
    db.session.commit()
    return todo

def update_todo(todo_id, title, content,finish):
    todo = get_todo_by_todo_id(todo_id)
    if not todo:
        raise TodoNotExistError

    todo.update(title, content,finish)
    return todo
