from datetime import datetime
from typing import Optional, ClassVar

from sqlmodel import SQLModel, Field, Column, Integer, ForeignKeyConstraint


class HistoricalPriceBase(SQLModel):
    """
    Base model for the 'HistoricalPrice' entity, establishing the fundamental attributes and constraints.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    flight_id: int = Field(
        sa_column=Column(Integer, nullable=True, default=None),
        description="Foreign key to the flight being monitored",
    )
    price: float = Field(description="Price of the flight at the given time")
    timestamp: datetime = Field(description="Timestamp of the price")


class HistoricalPrice(HistoricalPriceBase, table=True):
    """
    Represents a historical price in the database, extending HistoricalPriceBase for database integration.

    It includes additional attributes specific to database representation and relationships
    with other entities.
    """

    __tablename__ = "historical_price"
    __table_args__: ClassVar = (
        ForeignKeyConstraint(
            ["flight_id"],
            ["aviation.flight.id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        {"schema": "transaction"},
    )
