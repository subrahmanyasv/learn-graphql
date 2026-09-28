#app/schema.py

import typing
from app.db import get_todos, get_todos_by_user_id, get_users, get_user_by_id, create_todo, update_todo
import strawberry
from app.models import Todo, User, CreateTodoInput, UpdateTodoInput

@strawberry.type
class Query:
    @strawberry.field
    def todos(self, user_id: strawberry.ID = None ) -> list[Todo]:
        if user_id is not None:
            return get_todos_by_user_id(user_id)
        return get_todos()


    @strawberry.field
    def users(self) -> list[User]:
        return get_users()

    @strawberry.field
    def user(self, user_id: strawberry.ID) -> User | None:
        return get_user_by_id(user_id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_todo(self, input: CreateTodoInput) -> Todo:
        return create_todo(title=input.title, user_id=input.user_id)

    @strawberry.mutation
    def update_todo(self, input: UpdateTodoInput) -> Todo:
        return update_todo(todo_id=input.id, title=input.title, completed=input.completed)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
