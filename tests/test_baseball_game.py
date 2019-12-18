import pytest
from leetcode import baseball_game


@pytest.mark.parametrize(
    'ops,expected',
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    ],
)
def test_cal_points(ops, expected):
    assert baseball_game.cal_points(ops) == expected
