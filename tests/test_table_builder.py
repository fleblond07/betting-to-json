from common.table_builder import generate_table_from_betting_list
from domain.bet import BettingElement, BettingList, PossibleOutcome, Strategy

DEFAULT_BETTING_ELEMENTS = [
    BettingElement(
        id=1,
        team_1="PSG",
        team_2="Milan",
        odds_t1=2.32,
        odds_draw=3.31,
        odds_t2=2.32,
        choice=PossibleOutcome.TEAM_1,
        result=PossibleOutcome.TEAM_1,
        strategy=Strategy.RISKY,
    ),
    BettingElement(
        id=2,
        team_1="Italy",
        team_2="Norway",
        odds_t1=2.32,
        odds_draw=3.31,
        odds_t2=2.32,
        choice=PossibleOutcome.TEAM_1,
        result=PossibleOutcome.TEAM_2,
        strategy=Strategy.RISKY,
    ),
]
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
