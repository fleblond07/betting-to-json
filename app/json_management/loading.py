from domain.bet import BettingList, Strategy, BettingElement
from typing import Any, Optional


def json_to_betting_list(
    content_to_load: dict[str, Any], strategy_name: Strategy
) -> Optional[BettingList]:
    if strategy_name is Strategy.ALL:
        list_of_bets = []
        list_of_strategies = content_to_load.keys()
        for strategy in list_of_strategies:
            if strategy == "total":
                continue
            list_of_bets.extend(content_to_load[strategy])
    else:
        list_of_bets = content_to_load[strategy_name.value]
    if not list_of_bets:
        return None

    return BettingList(
        bets=[
            BettingElement(
                **bet,
                strategy=strategy_name.value,
            )
            for bet in list_of_bets
            if bet
        ]
    )
