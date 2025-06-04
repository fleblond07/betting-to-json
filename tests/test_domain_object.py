import pytest
from domain.bet import Strategy


class TestDomainObjectValidation:
    @pytest.mark.parametrize(
        "input, expected", [("safe", Strategy.SAFE), ("risky", Strategy.RISKY)]
    )
    def test_strategy_enum(self, input: str, expected: Strategy) -> None:
        assert Strategy(input) == expected

    @pytest.mark.parametrize("model, input", [(Strategy, "unknown")])
    def test_wrong_enum(self, model, input) -> None:
        with pytest.raises(ValueError):
            model(input)
