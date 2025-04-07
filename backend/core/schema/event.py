from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from core.schema.map import MapReadSchema
from core.schema.match import MatchReadSchema


class OutComeSchema(BaseModel):
    name: str = Field(max_length=32)
    coefficient: Decimal = Field(max_digits=10, decimal_places=2)


class OutComeReadSchema(OutComeSchema):
    id: int = Field(gt=0)


class OutComeCreateSchema(OutComeSchema):
    ...


class OutComeUpdateSchema(OutComeSchema):
    ...


class EventSchema(BaseModel):
    name: str = Field(max_length=32, min_length=1)


class EventReadSchema(EventSchema):
    id: int
    match: MatchReadSchema
    map: MapReadSchema | None = None
    first_outcome: OutComeSchema
    second_outcome: OutComeSchema
    created_at: datetime
    updated_at: datetime


class EventCreateSchema(EventSchema):
    match_id: int = Field(gt=0)
    map_id: int = Field(gt=0)
    first_outcome: OutComeCreateSchema
    second_outcome: OutComeCreateSchema
    updated_by: int | None = Field(None, exclude=True)


class EventUpdateSchema(EventSchema):
    match_id: int | None = Field(None, gt=0)
    map_id: int | None = Field(None, gt=0)
    first_outcome_id: int | None = Field(None, gt=0)
    second_outcome_id: int | None = Field(None, gt=0)
