from pydantic import BaseModel, Field, field_validator

from core.schema.game import GameReadSchema
from core.utils.files import add_base_url


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
    icon_path: str

    @field_validator("icon_path")
    @classmethod
    def icon_path_validate(cls, v: str):
        return add_base_url(v)
