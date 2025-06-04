from domain.bet import BettingList, Strategy, BettingElement
from typing import Any, Optional


def json_to_betting_list(
    content_to_load: dict[str, Any], strategy_name: Strategy
) -> Optional[BettingList]:
    list_of_bets = content_to_load[strategy_name.value]
    if len(list_of_bets) <= 1:
        return None
    return BettingList(
        bets=[
            BettingElement(
                **bet,
                strategy=strategy_name,
            )
            for bet in list_of_bets
        ]
    )
