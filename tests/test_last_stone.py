import pytest
from leetcode import last_stone


@pytest.mark.parametrize(
    'stones,expected',
    [
        ([2, 7, 4, 1, 8, 1], 1),
    ],
)
def test_last_stone(stones, expected):
    assert last_stone.last_stone(stones) == expected
