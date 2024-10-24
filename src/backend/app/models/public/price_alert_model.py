from datetime import datetime
from typing import ClassVar, Optional

from sqlmodel import Column, Field, ForeignKeyConstraint, Integer, SQLModel


class PriceAlertBase(SQLModel):
    """
    Base model for the 'PriceAlert' entity, establishing the fundamental attributes and constraints.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(
        sa_column=Column(Integer, nullable=True, default=None),
        description="Foreign key to the user who created the alert",
    )
    flight_id: int = Field(
        sa_column=Column(Integer, nullable=True, default=None),
        description="Foreign key to the flight being monitored",
    )
    threshold: float = Field(description="Price to trigger the alert")
    status: bool = Field(description="Status of the alert")
    created_at: datetime = Field(default=datetime.now(), description="Created at")
    updated_at: datetime = Field(default=datetime.now(), description="Updated at")


class PriceAlert(PriceAlertBase, table=True):
    """
    Represents a price alert in the database, extending PriceAlertBase for database integration.

    It includes additional attributes specific to database representation and relationships
    with other entities.
    """

    __tablename__ = "price_alert"
    __table_args__: ClassVar = (
        ForeignKeyConstraint(
            ["user_id"], ["public.user.id"], ondelete="CASCADE", onupdate="CASCADE"
        ),
        ForeignKeyConstraint(
            ["flight_id"],
            ["public.flight.id"],
            ondelete="NO ACTION",
            onupdate="CASCADE",
        ),
        {"schema": "public"},
    )
