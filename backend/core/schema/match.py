from datetime import datetime

from pydantic import BaseModel, Field, model_validator, field_validator
from pydantic_core import PydanticCustomError

class MatchSchema(BaseModel):
    tournament_id: int = Field(gt=0)
    first_team_id: int = Field(gt=0)
    second_team_id: int = Field(gt=0)
    score: list[int] = Field(min_length=0, max_length=2)
    best_of: int = Field(gt=0)
    date_start: datetime | None = None
    date_end: datetime | None = None

    @model_validator(mode="after")
    def validate_dates(self):
        if self.date_end and self.date_start and self.date_end < self.date_start:
            raise PydanticCustomError(
                "date_error",
                "the end date cannot be earlier than the start date",
            )
        return self

    @model_validator(mode="after")
    def validate_team_not_equals(self):
        if self.first_team_id == self.second_team_id and (self.first_team_id or self.second_team_id):
            raise PydanticCustomError(
                "team_equal_error",
                "the commands cannot be the same",
            )
        return self

    @field_validator("score", mode="before")
    @classmethod
    def validate_score_items(cls, score: list[int]):
        if score and any(x < 0 for x in score):
            raise PydanticCustomError(
                "the_score_error",
                "all account values must be greater than or equal to zero",
            )
        return score

class MatchCreateSchema(MatchSchema):
    date_end: None = Field(exclude=True, default=None)


class MatchReadSchema(MatchSchema):
    id: int


class MatchUpdateSchema(MatchSchema):
    tournament_id: int | None = Field(None, gt=0)
    first_team_id: int | None  = Field(None, gt=0)
    second_team_id: int | None = Field(None, gt=0)
    score: list[int] | None = Field(None, min_length=0, max_length=2)
    best_of: int | None = Field(None, gt=0)
