from pydantic import BaseModel


class MapSchema(BaseModel):
    match_id: int
    score: list[int] = [0, 0]


class MapReadSchema(MapSchema):
    id: int
    winner_id: int | None = None


class MapUpdateSchema(MapSchema):
    winner_id: int | None = None
    match_id: int | None = None


class MapCreateSchema(MapSchema):
    ...
