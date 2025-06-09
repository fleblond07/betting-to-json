# TO FINISH TESTING THIS
# def start_read_mode(filename: str = "json/default_json.json"):
#     data = read_json_file(file_name="json/default_json.json")
#     if not data:
#         return None

#     betting_list: Optional[BettingList] = json_to_betting_list(
#         content_to_load=data, strategy_name=Strategy.RISKY
#     )
#     if not betting_list:
#         return None

#     table = generate_table_from_betting_list(
#         betting_list=betting_list, table_title="Bet history"
#     )

#     console.print(table)
#     return betting_list


def test_start_happy_path():
    start_read_mode(filename="app/json/defula")
