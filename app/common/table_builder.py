from rich.table import Table

from common.utils import is_winner
from domain.bet import BettingElement, BettingList


def generate_table_from_betting_list(
    betting_list: BettingList, table_title: str = "Bet history"
):
    number_of_wins = 0

    table = Table(title=table_title)

    for key in BettingElement.model_fields.keys():
        table.add_column(key.capitalize())

    for bet in betting_list.bets:
        if is_winner(bet):
            number_of_wins += 1
        table.add_row(*[str(value) for value in bet.model_dump().values()])

    return table
