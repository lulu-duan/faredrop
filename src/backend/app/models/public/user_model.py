from datetime import datetime
from typing import ClassVar, Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    """
    Base model for the 'User' entity, establishing the fundamental attributes and constraints.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(description="Name of the user")
    username: str = Field(description="Username of the user")
    email: EmailStr = Field(description="Email of the user")
    created_at: datetime = Field(
        default=datetime.now(), description="The timestamp the user record was created"
    )
    updated_at: datetime = Field(
        default=datetime.now(),
        description="The timestamp the user record was last updated",
    )


class User(UserBase, table=True):
    """
    Represents a user in the database, extending UserBase for database integration.

    It includes additional attributes specific to database representation and relationships
    with other entities.
    """

    __tablename__ = "user"
    __table_args__: ClassVar = {"schema": "public"}
    hashed_password: str | None = Field(
        nullable=False, index=True, description="Hashed password of the user"
    )
