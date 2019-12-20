import pytest
from leetcode import jewels_and_stones


@pytest.mark.parametrize(
    'j,s,expected',
    [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
    ],
)
def test_jewels_and_stones(j, s, expected):
    assert jewels_and_stones.jewels_and_stones(j, s) == expected
