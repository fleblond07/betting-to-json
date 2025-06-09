from common.exception import UnknownError
from typing import Any
from domain.bet import BettingElement, BettingList, Strategy
from json_management.loading import json_to_betting_list
import pytest
from json_management.open import read_json_file

VALID_BETTING_LIST_DICT: dict[str, list[Any]] = {
    "risky": [
        {
            "id": 1,
            "team_1": "Team1",
            "team_2": "Team2",
            "odds_t1": 2.13,
            "odds_draw": 3.21,
            "odds_t2": 2.58,
            "choice": "team_1",
            "result": "team_1",
        },
        {
            "id": 2,
            "team_1": "Team1",
            "team_2": "Team2",
            "odds_t1": 3.13,
            "odds_draw": 1.21,
            "odds_t2": 4.58,
            "choice": "draw",
            "result": "team_1",
        },
    ]
}

EMPTY_BETTING_LIST_DICT: dict = {"risky": []}


class TestJsonFunctionnalities:
    def test_open_valid_json_file(self):
        data = read_json_file("app/json/default_json.json")
        assert data is not None

    def test_open_invalid_json_file(self):
        with pytest.raises(FileNotFoundError):
            read_json_file("does/not/exist.json")

    def test_empty_json_file(self):
        with pytest.raises(UnknownError):
            read_json_file("app/json/empty_json.json")

    def test_load_valid_betting_list(self):
        result = json_to_betting_list(VALID_BETTING_LIST_DICT, Strategy("risky"))
        assert type(result) is BettingList
        assert result.bets[0] == BettingElement(
            id=1,
            team_1="Team1",
            team_2="Team2",
            odds_t1=2.13,
            odds_draw=3.21,
            odds_t2=2.58,
            choice="team_1",
            result="team_1",
            strategy="risky",
        )

    def test_load_empty_betting_list(self):
        result = json_to_betting_list(EMPTY_BETTING_LIST_DICT, Strategy("risky"))
        assert result is None
