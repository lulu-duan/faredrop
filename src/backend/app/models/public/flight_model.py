from datetime import datetime
from typing import ClassVar, Optional

from sqlmodel import Field, SQLModel


class FlightBase(SQLModel):
    """
    Base model for the 'Flight' entity, establishing the fundamental attributes and constraints.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    flight_number: str = Field(description="Flight number")
    name: str = Field(description="Name of the flight")
    origin: str = Field(description="Departure airport code")
    destination: str = Field(description="Arrival airport code")
    status: str = Field(description="Status of the flight")
    departure_time: datetime = Field(description="Departure time of the flight")
    arrival_time: datetime = Field(description="Arrival time of the flight")
    price: float = Field(description="Current price of the flight")
    created_at: datetime = Field(
        default=datetime.now(),
        description="The timestamp the flight record was created",
    )
    updated_at: datetime = Field(
        default=datetime.now(),
        description="The timestamp the flight record was last updated",
    )


class Flight(FlightBase, table=True):
    """
    Represents a flight in the database, extending FlightBase for database integration.

    It includes additional attributes specific to database representation and relationships
    with other entities.
    """

    __tablename__ = "flight"
    __table_args__: ClassVar = {"schema": "public"}
