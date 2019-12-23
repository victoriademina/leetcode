import pytest
from leetcode import return_to_origin


@pytest.mark.parametrize(
    'moves,expected',
    [
        ("UD", True),
        ("LL", False),
        ("UU", False),
    ],
)
def test_repeated_element(moves, expected):
    assert return_to_origin.return_to_origin(moves) == expected
