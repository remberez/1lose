from pydantic import BaseModel, Field

from core.schema.game import GameReadSchema


class EventTypeSchema(BaseModel):
    code: str = Field(max_length=32)
    name: str = Field(max_length=64)
    game_id: int = Field(gt=0)


class EventTypeCreateSchema(EventTypeSchema):
    ...


class EventTypeReadSchema(EventTypeSchema):
    game: list["GameReadSchema"]


class EvenTypeUpdateSchema(EventTypeSchema):
    ...
