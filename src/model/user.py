from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    full_name: str


class CreateUserRequest(BaseModel):
    email: str
    full_name: str
