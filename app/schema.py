#app/schema.py

import typing
from app.db import get_todos, get_todos_by_user_id, get_users, get_user_by_id
import strawberry
from app.models import Todo, User

@strawberry.type
class Query:
    @strawberry.field
    def todos(self, user_id: strawberry.ID | None ) -> list[Todo]:
        if user_id is not None:
            return get_todos_by_user_id(user_id)
        return get_todos()


    @strawberry.field
    def users(self) -> list[User]:
        return get_users()

    @strawberry.field
    def user(self, user_id: strawberry.ID) -> User | None:
        return get_user_by_id(user_id)

schema = strawberry.Schema(query=Query)

