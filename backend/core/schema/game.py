from pydantic import BaseModel, Field


class GameSchema(BaseModel):
    name: str = Field(max_length=25)
    description: str


class GameCreateSchema(GameSchema): ...


class GameReadSchema(GameSchema):
    id: int


class GameUpdateSchema(GameSchema): ...
