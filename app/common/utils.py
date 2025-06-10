from domain.bet import BettingElement


def is_winner(bet: BettingElement):
    return True if bet.choice == bet.result else False
