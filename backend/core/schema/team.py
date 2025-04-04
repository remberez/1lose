from pydantic import BaseModel, Field


class EATeamSchema(BaseModel):
    name: str = Field(max_length=32)
    description: str


class EATeamCreateSchema(EATeamSchema): ...


class EATeamUpdateSchema(BaseModel):
    name: str | None = Field(None, max_length=32)
    description: str | None = None


class EATeamReadSchema(BaseModel):
    id: int
