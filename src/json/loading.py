from domain.bet import BettingElement, BettingList, Strategy
from typing import Any


def json_to_betting_list(
    content_to_load: dict[str, Any], strategy_name: Strategy
) -> BettingList:
    json_bet_list = content_to_load[strategy_name.value]
    list_of_elements = [
        BettingElement(
            id=bet.get("id"),
            team_1=bet.get("team_1"),
            team_2=bet.get("team_2"),
            odds_t1=bet.get("odds_t1"),
            odds_draw=bet.get("odds_draw"),
            odds_t2=bet.get("odds_t2"),
            choice=bet.get("choice"),
            result=bet.get("result"),
            strategy=strategy_name,
        )
        for bet in json_bet_list
    ]

    return BettingList(list_of_elements)
