from decimal import Decimal

from pydantic import BaseModel, Field

from core.const.bet_status import BetStatus


class BetSchema(BaseModel):
    event_id: int = Field(gt=0)
    amount: Decimal = Field(max_digits=12, decimal_places=2)


class BetReadSchema(BetSchema):
    id: int = Field(gt=0)
    event_id: int = Field(exclude=True)
    coefficient: Decimal = Field(max_digits=12, decimal_places=2)
    possible_gain: Decimal = Field(max_digits=12, decimal_places=2)
    bet_status: BetStatus


class BetCreateSchema(BetSchema):
    ...


class BetUpdateSchema(BetSchema):
    bet_status: BetStatus
