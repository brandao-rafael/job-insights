from unittest.mock import mock_open, patch
import pytest
from src.pre_built.counter import count_ocurrences


@pytest.fixture
def mocked_data():
    return """
    banana,
    Pêra,
    maçã,
    Banana,
    banana,
    pêra,
    banana,
    Banana
    """


def test_counter(mocked_data):
    with patch("builtins.open", mock_open(read_data=mocked_data)):
        assert count_ocurrences("/dir/file.csv", "banana") == 5
