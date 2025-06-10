from common.table_builder import generate_table_from_betting_list
from domain.bet import BettingList, Strategy
from typing import Optional
from json_management.loading import json_to_betting_list
from json_management.open import read_json_file
from rich.console import Console

console = Console()


def start_read_mode(
    filename: Optional[str] = "app/json/default_json.json",
    strategy: Strategy = Strategy.ALL,
):
    if not filename:
        filename = "app/json/default_json.json"

    data = read_json_file(file_name=filename)

    betting_list: Optional[BettingList] = json_to_betting_list(
        content_to_load=data, strategy_name=strategy
    )
    if not betting_list or not betting_list.bets:
        return None

    table_summary, table_total = generate_table_from_betting_list(
        betting_list=betting_list, table_title="Bet history"
    )
    console.print(table_total)
    console.print(table_summary)
    return betting_list
