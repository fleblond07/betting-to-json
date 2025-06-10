from domain.bet import BettingElement, PossibleOutcome, Strategy


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
