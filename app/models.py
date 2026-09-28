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
        

@strawberry.input
class CreateTodoInput:
    title: str = strawberry.field(description="The title of the todo item")
    user_id: strawberry.ID = strawberry.field(description="The ID of the user who owns the todo item")


@strawberry.input
class UpdateTodoInput:
    id: strawberry.ID = strawberry.field(description="The ID of the todo item to update")
    title: typing.Optional[str] = strawberry.field(description="The new title of the todo item", default=None)
    completed: typing.Optional[bool] = strawberry.field(description="The new completion status of the todo item", default=None)
