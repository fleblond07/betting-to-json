from src.input_management import user_select_betting_mode
## TODO:
# Init all the stuff
# Read bets
# Write bets
# Total profit for each strategies
# Weekly totals
# Presentation screen
# JSON TO MD


def main():
    try:
        print("Hi!")
        user_select_betting_mode()
    except Exception as e:
        print(f"Oops something wrong happened: {e}")
        exit()


if __name__ == "__main__":
    main()
