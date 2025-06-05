from datetime import datetime

from pydantic import BaseModel, Field, model_validator, field_validator
from pydantic_core import PydanticCustomError

from core.schema.team import EATeamReadSchema
from core.schema.tournament import TournamentReadSchema
from core.schema.event import EventReadSchema


class MatchSchema(BaseModel):
    best_of: int = Field(gt=0)
    date_start: datetime | None = None
    date_end: datetime | None = None
    tournament_id: int = Field(gt=0)
    first_team_id: int = Field(gt=0)
    second_team_id: int = Field(gt=0)

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
        if self.first_team_id == self.second_team_id and (
            self.first_team_id or self.second_team_id
        ):
            raise PydanticCustomError(
                "team_equal_error",
                "the commands cannot be the same",
            )
        return self


class MatchCreateSchema(MatchSchema):
    date_end: None = Field(exclude=True, default=None)


class MatchReadSchema(MatchSchema):
    id: int
    tournament: TournamentReadSchema
    first_team: EATeamReadSchema
    second_team: EATeamReadSchema
    tournament_id: int = Field(gt=0, exclude=True)
    first_team_id: int = Field(gt=0, exclude=True)
    second_team_id: int = Field(gt=0, exclude=True)
    win_event: EventReadSchema | None = None
    score: list[int] | None = Field(None, min_length=0, max_length=2)


class MatchUpdateSchema(MatchSchema):
    tournament_id: int | None = Field(None, gt=0)
    first_team_id: int | None = Field(None, gt=0)
    second_team_id: int | None = Field(None, gt=0)
    score: list[int] | None = Field(None, min_length=0, max_length=2)
    best_of: int | None = Field(None, gt=0)
    win_event_id: int | None = Field(None, gt=0)

    @field_validator("score", mode="before")
    @classmethod
    def validate_score_items(cls, score: list[int]):
        if score and any(x < 0 for x in score):
            raise PydanticCustomError(
                "the_score_error",
                "all account values must be greater than or equal to zero",
            )
        return score


class MathFilterSchema(BaseModel):
    is_live: bool | None = None
    game_id: int | None = None
