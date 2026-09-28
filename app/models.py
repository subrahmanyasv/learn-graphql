#app/models.py
import strawberry
import typing

@strawberry.type
class User:
    id: strawberry.ID
    username: str
    email: str

    @strawberry.field
    def todos(self) -> typing.List["Todo"]:
        from app.db import get_todos_by_user_id
        return get_todos_by_user_id(self.id)

@strawberry.type
class Todo:
    id: strawberry.ID
    title: str
    completed: bool = False
    user_id: strawberry.ID

    @strawberry.field
    def user(self) -> User:
        from app.db import get_user_by_id
        return get_user_by_id(self.user_id)
        

