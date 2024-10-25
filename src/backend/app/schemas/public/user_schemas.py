from sqlmodel import SQLModel


class IUserCreate(SQLModel):
    name: str
    username: str
    email: str
    password: str
