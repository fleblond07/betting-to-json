from common.table_builder import generate_table_from_betting_list
from domain.bet import BettingElement, BettingList
from resource import DEFAULT_BETTING_ELEMENTS

DEFAULT_BETTING_LIST = BettingList(bets=DEFAULT_BETTING_ELEMENTS)


def test_build_default_table():
    actual_table = generate_table_from_betting_list(
        betting_list=DEFAULT_BETTING_LIST, table_title="Toto"
    )
    assert actual_table.title == "Toto"
    assert [column.header.lower() for column in actual_table.columns] == list(
        BettingElement.model_fields.keys()
    )
    assert len(actual_table.rows) == 2
