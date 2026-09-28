#db.py
from app.models import Todo, User

def get_todos() -> list[Todo]:
    # This is a placeholder implementation. In a real application, you would fetch data from a database.
    return [
        Todo(id="1", title="Buy groceries", completed=False, user_id="1"),
        Todo(id="2", title="Walk the dog", completed=True, user_id="1"),
        Todo(id="3", title="Read a book", completed=False, user_id="2"),
        Todo(id="4", title="Write code", completed=True, user_id="2"),
        Todo(id="5", title="Exercise", completed=False, user_id="3"),
        Todo(id="6", title="Cook dinner", completed=True, user_id="3"),
    ]


def get_users() -> list[User]:
    # This is a placeholder implementation. In a real application, you would fetch data from a database.
    return [
        User(id="1", username="john_doe", email="john.doe@example.com"),
        User(id="2", username="jane_smith", email="jane.smith@example.com"),
        User(id="3", username="alice_jones", email="alice.jones@example.com"),
        User(id="4", username="bob_brown", email="bob.brown@example.com"),
        User(id="5", username="charlie_white", email="charlie.white@example.com"),
    ]


def get_user_by_id(user_id: str) -> User:
    # This is a placeholder implementation. In a real application, you would fetch data from a database.
    users = get_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

def get_todos_by_user_id(user_id: str) -> list[Todo]:
    # This is a placeholder implementation. In a real application, you would fetch data from a database.
    todos = get_todos()
    return [todo for todo in todos if todo.user_id == user_id]

def get_todo_by_id(todo_id: str) -> Todo:
    # This is a placeholder implementation. In a real application, you would fetch data from a database.
    todos = get_todos()
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None
