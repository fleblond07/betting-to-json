from pydantic.dataclasses import dataclass
from enum import Enum
from typing import Optional


class Strategy(Enum):
    SAFE = "safe"
    RISKY = "risky"


class PossibleOutcome(Enum):
    TEAM_1 = "team_1"
    TEAM_2 = "team_2"
    DRAW = "draw"


@dataclass
class BettingElement:
    id: int
    team_1: str
    team_2: str
    odds_t1: float
    odds_draw: float
    odds_t2: float
    choice: Optional[PossibleOutcome]
    result: Optional[PossibleOutcome]
    strategy: Strategy
