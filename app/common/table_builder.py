from rich.table import Table

from domain.bet import BettingElement, BettingList


def generate_table_from_betting_list(
    betting_list: BettingList, table_title: str = "Bet history"
):
    table = Table(title=table_title)

    for key in BettingElement.model_fields.keys():
        table.add_column(key.capitalize())

    for bet in betting_list.bets:
        table.add_row(*[str(value) for value in bet.model_dump().values()])

    return table
