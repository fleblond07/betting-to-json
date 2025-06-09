from common.table_builder import generate_table_from_betting_list
from domain.bet import BettingList, Strategy
from typing import Optional
from json_management.loading import json_to_betting_list
from json_management.open import read_json_file
from rich.console import Console

console = Console()


def start_read_mode(filename: str = "json/default_json.json"):
    data = read_json_file(file_name="json/default_json.json")
    if not data:
        return None

    betting_list: Optional[BettingList] = json_to_betting_list(
        content_to_load=data, strategy_name=Strategy.RISKY
    )
    if not betting_list:
        return None

    table = generate_table_from_betting_list(
        betting_list=betting_list, table_title="Bet history"
    )

    console.print(table)
    return betting_list
