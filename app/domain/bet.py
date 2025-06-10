from enum import Enum
from typing import Optional

from pydantic.main import BaseModel


class Strategy(Enum):
    SAFE = "safe"
    RISKY = "risky"
    EMPTY = "empty"
    ALL = "all"


class PossibleOutcome(Enum):
    TEAM_1 = "team_1"
    TEAM_2 = "team_2"
    DRAW = "draw"


class BettingElement(BaseModel):
    id: int
    team_1: str
    team_2: str
    odds_t1: float
    odds_draw: float
    odds_t2: float
    choice: Optional[PossibleOutcome]
    result: Optional[PossibleOutcome]
    strategy: Strategy


class BettingList(BaseModel):
    bets: list[BettingElement]
