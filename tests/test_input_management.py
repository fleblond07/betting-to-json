from flow.input_management import user_select_betting_mode


class TestUserChoiceMode:
    def test_read_mode(self, monkeypatch):
        inputs = iter(["read", "app/json/default_json.json"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        user_select_betting_mode()

    def test_place_mode(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "place")
        assert user_select_betting_mode() == "place"

    def test_modify_mode(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "modify")
        assert user_select_betting_mode() == "modify"
