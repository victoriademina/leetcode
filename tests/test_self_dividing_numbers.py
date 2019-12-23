import pytest
from leetcode import self_dividing_numbers


@pytest.mark.parametrize(
    'left,right,expected',
    [
        (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
    ],
)
def test_self_dividing_numbers(left, right, expected):
    assert self_dividing_numbers.self_dividing_numbers(left, right) == expected
