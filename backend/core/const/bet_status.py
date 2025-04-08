from enum import Enum


class BetStatus(Enum):
    ACTIVE = "active"
    WON = "won"
    LOST = "lost"
    SOLD = "sold"
    CANCELED = "canceled"
