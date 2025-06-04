from common.exception import UnknownError
import pytest


class TestException:
    def test_unknown_error_default(self):
        with pytest.raises(UnknownError) as exception:
            raise UnknownError(message=None)
        assert str(exception.value.message) == "Unknown error occurred"

    def test_unknown_error_with_custom_message(self):
        custom_message = "This is a custom exception message"
        with pytest.raises(UnknownError) as exception:
            raise UnknownError(message=custom_message)
        assert str(exception.value.message) == custom_message
