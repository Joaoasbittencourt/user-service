from pydantic import UUID4, BaseModel


class UserPath(BaseModel):
    user_id: UUID4


class User(BaseModel):
    id: UUID4
    email: str
    name: str


class CreateUserDTO(BaseModel):
    email: str
    name: str


class GetUsersResponse(BaseModel):
    users: list[User]
