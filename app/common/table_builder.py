from rich.table import Table

from common.utils import is_winner
from domain.bet import BettingElement, BettingList


def generate_table_from_betting_list(
    betting_list: BettingList, table_title: str = "Bet history"
):
    number_of_wins = 0

    table_summary = Table(title=table_title)

    for key in BettingElement.model_fields.keys():
        table_summary.add_column(key.capitalize())

    for bet in betting_list.bets:
        if is_winner(bet):
            number_of_wins += 1
        table_summary.add_row(*[str(value) for value in bet.model_dump().values()])
    table_total = _generate_total_table_from_betting_list(number_of_win=number_of_wins)
    return table_summary, table_total


def _generate_total_table_from_betting_list(
    number_of_win: int = 0,
):
    table = Table(title="TOTAL")

    keys = ["PLACED", "WIN", "LOST", "GAIN"]

    for key in keys:
        table.add_column(key.capitalize())
    totals = {"PLACED": 0, "WIN": number_of_win, "LOST": 0, "GAIN": 0}
    table.add_row(*totals)

    return table
