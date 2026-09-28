#app/schema.py

import typing
from app.db import get_todos, get_todos_by_user_id
import strawberry
from app.models import Todo

@strawberry.type
class Query:
    todos: typing.List[Todo] = strawberry.field(resolver = get_todos)
    get_todos_by_user_id: typing.List[Todo] = strawberry.field( resolver = get_todos_by_user_id )


schema = strawberry.Schema(query=Query)

