from pydantic import BaseModel, Field


class MapSchema(BaseModel):
    match_id: int
    score: list[int]


class MapReadSchema(MapSchema):
    id: int
    winner_id: int | None = None


class MapUpdateSchema(MapSchema):
    winner_id: int | None = None
    match_id: int | None = None


class MapCreateSchema(MapSchema):
    ...
