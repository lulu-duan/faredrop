from datetime import datetime
from typing import ClassVar, Optional

from sqlmodel import Field, SQLModel


class FlightBase(SQLModel):
    """
    Base model for the 'Flight' entity, establishing the fundamental attributes and constraints.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    flight_number: str = Field(description="Flight number", nullable=False)
    name: str = Field(description="Name of the flight", nullable=True)
    origin: str = Field(description="Departure airport code", nullable=False)
    destination: str = Field(description="Arrival airport code", nullable=False)
    status: str = Field(description="Status of the flight", nullable=True)
    departure_time: datetime = Field(
        description="Departure time of the flight", nullable=True
    )
    arrival_time: datetime = Field(
        description="Arrival time of the flight", nullable=True
    )
    price: float = Field(description="Current price of the flight", nullable=True)
    created_at: datetime = Field(
        default=datetime.now(),
        description="The timestamp the flight record was created",
        nullable=False,
    )
    updated_at: datetime = Field(
        default=datetime.now(),
        description="The timestamp the flight record was last updated",
        nullable=False,
    )


class Flight(FlightBase, table=True):
    """
    Represents a flight in the database, extending FlightBase for database integration.

    It includes additional attributes specific to database representation and relationships
    with other entities.
    """

    __tablename__ = "flight"
    __table_args__: ClassVar = {"schema": "public"}
