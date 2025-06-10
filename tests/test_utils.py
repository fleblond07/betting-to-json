from common.utils import is_winner
from resource import DEFAULT_BETTING_ELEMENTS


def test_is_winner_true():
    assert is_winner(DEFAULT_BETTING_ELEMENTS[0]) is True


def test_is_winner_false():
    assert is_winner(DEFAULT_BETTING_ELEMENTS[1]) is False
