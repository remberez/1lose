from datetime import datetime

from pydantic import BaseModel, Field

from core.schema.map import MapReadSchema
from core.schema.match import MatchReadSchema
from core.schema.user import UserReadSchema


class OutComeSchema(BaseModel):
    name: str = Field(max_length=32)
    coefficient: float = Field(max_digits=10, decimal_places=2)


class OutComeReadSchema(OutComeSchema):
    ...


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
    create_at: datetime
    updated_at: datetime
    updated_by: UserReadSchema


class EventCreateSchema(EventSchema):
    match_id: int = Field(gt=0)
    map_id: int = Field(gt=0)
    first_outcome_id: int = Field(gt=0)
    second_outcome_id: int = Field(gt=0)


class EventUpdateSchema(EventSchema):
    match_id: int | None = Field(None, gt=0)
    map_id: int | None = Field(None, gt=0)
    first_outcome_id: int | None = Field(None, gt=0)
    second_outcome_id: int | None = Field(None, gt=0)
