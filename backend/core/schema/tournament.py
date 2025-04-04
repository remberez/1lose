from pydantic import BaseModel, Field
from .game import GameReadSchema


class TournamentSchema(BaseModel):
    name: str = Field(max_length=64)
    description: str


class TournamentReadSchema(TournamentSchema):
    id: int
    game: GameReadSchema


class TournamentCreateSchema(TournamentSchema):
    game_id: int


class TournamentUpdateSchema(TournamentSchema):
    name: str | None = Field(None, max_length=64)
    description: str | None = None
    game_id: int | None = None
