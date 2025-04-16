from pydantic import BaseModel, Field, field_validator
from core.utils.files import add_base_url


class GameSchema(BaseModel):
    name: str = Field(max_length=25)
    description: str


class GameCreateSchema(GameSchema): ...


class GameReadSchema(GameSchema):
    id: int
    icon_path: str = Field()

    @field_validator("icon_path")
    @classmethod
    def icon_path_validate(cls, v: str):
        return add_base_url(v)


class GameUpdateSchema(GameSchema):
    name: str | None = Field(None, max_length=25)
    description: str | None = None
