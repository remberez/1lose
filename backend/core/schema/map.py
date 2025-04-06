from pydantic import BaseModel


class MapSchema(BaseModel):
    match_id: int
    score: list[int]
    winner_id: int


class MapReadSchema(MapSchema):
    id: int


class MapUpdateSchema(MapSchema):
    ...


class MapCreateSchema(MapSchema):
    ...
