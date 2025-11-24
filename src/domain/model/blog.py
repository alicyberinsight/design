from pydantic import BaseModel


class Blog(BaseModel):
    id: int
    title: str
    content: str


class CreateBlogRequest(BaseModel):
    title: str
    content: str
