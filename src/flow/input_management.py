from domain.mode import BettingMode
from read import start_read_mode
from place import start_place_mode
from modify import start_modify_mode


def user_select_betting_mode():
    mode = input("What would you like to do (read, place, modify)")
    match BettingMode(mode):
        case BettingMode.READ:
            return start_read_mode()
        case BettingMode.PLACE:
            return start_place_mode()
        case BettingMode.MODIFY:
            return start_modify_mode()
        case _:
            raise Exception("Unkown choice inputed for read/place/modify")
