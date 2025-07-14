from flow.input_management import user_select_betting_mode


def main():
    try:
        user_select_betting_mode()
    except Exception as e:
        print(f"Oops something wrong happened: {e}")
        exit()


if __name__ == "__main__":
    main()
