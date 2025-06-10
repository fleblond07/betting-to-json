from domain.bet import BettingElement, BettingList, Strategy
from read import start_read_mode

EXPECTED_ALL_DICT = [
    {
        "id": 1,
        "team_1": "Paris SG",
        "team_2": "Inter Milan",
        "odds_t1": 2.3,
        "odds_draw": 3.34,
        "odds_t2": 3.1,
        "result": "team_1",
        "choice": "team_1",
        "strategy": Strategy.ALL,
    },
    {
        "id": 1,
        "team_1": "Paris SG",
        "team_2": "Inter Milan",
        "odds_t1": 2.3,
        "odds_draw": 3.34,
        "odds_t2": 3.1,
        "result": "team_1",
        "choice": "team_1",
        "strategy": Strategy.ALL,
    },
]


def test_start_happy_path():
    expected = BettingList(bets=[BettingElement(**row) for row in EXPECTED_ALL_DICT])
    actual = start_read_mode()
    assert actual == expected


def test_empty_strategy():
    assert (
        start_read_mode(filename="app/json/default_json.json", strategy=Strategy.EMPTY)
        is None
    )
