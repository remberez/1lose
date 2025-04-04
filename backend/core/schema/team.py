from pydantic import BaseModel, Field

from core.schema.game import GameReadSchema


class EATeamSchema(BaseModel):
    name: str = Field(max_length=32)
    game_id: int


class EATeamCreateSchema(EATeamSchema): ...


class EATeamUpdateSchema(EATeamSchema):
    name: str | None = Field(None, max_length=32)


class EATeamReadSchema(BaseModel):
    id: int
    name: str = Field(max_length=32)
    game: GameReadSchema
