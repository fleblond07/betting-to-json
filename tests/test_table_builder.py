from common.table_builder import generate_table_from_betting_list
from domain.bet import BettingElement, BettingList
from resource import DEFAULT_BETTING_ELEMENTS

DEFAULT_BETTING_LIST = BettingList(bets=DEFAULT_BETTING_ELEMENTS)


def test_build_default_table():
    table_summary, table_total = generate_table_from_betting_list(
        betting_list=DEFAULT_BETTING_LIST, table_title="Toto"
    )
    assert table_summary.title == "Toto"
    assert [column.header.lower() for column in table_summary.columns] == list(
        BettingElement.model_fields.keys()
    )
    assert len(table_summary.rows) == 2
