from http import HTTPStatus
from src.dto import (
    UserPath,
    CreateUserDTO,
    GetUsersResponse,
    User,
)
from src.services import (
    create_user,
    delete_user,
    get_user,
    get_users,
)
from src.errors import NotFoundException
from src.state import AppState

ctx = AppState()
app = ctx.app


@app.get("/users/<uuid:user_id>", responses={200: User}, description="Get a User by id")
def get_user_handler(path: UserPath):
    with ctx.engine.connect() as conn:
        user = get_user(conn, path.store_id)
        if user is None:
            raise NotFoundException(f"User {path.store_id} not found")
        return user, HTTPStatus.OK


@app.get("/users", responses={200: GetUsersResponse}, description="Get all users")
def get_users_handler():
    with ctx.engine.connect() as conn:
        rows = get_users(conn)
        return GetUsersResponse(users=list(rows)).model_dump(), HTTPStatus.OK


@app.post(
    "/users",
    responses={201: User},
    description="Create a User",
)
def post_users_handler(body: CreateUserDTO):
    with ctx.engine.connect() as conn:
        user = create_user(conn, body)
        return user, HTTPStatus.CREATED


@app.delete(
    "/users/<uuid:user_id>",
    description="Deletes a user by id",
)
def delete_users_handler(path: UserPath):
    with ctx.engine.connect() as conn:
        delete_user(conn, path.user_id)
        return {}, HTTPStatus.NO_CONTENT


@app.errorhandler(Exception)
def bad_request_handler(e):
    return {"error": str(e)}, HTTPStatus.BAD_REQUEST


@app.errorhandler(NotFoundException)
def not_found_handler(e):
    return {"error": str(e)}, HTTPStatus.NOT_FOUND
