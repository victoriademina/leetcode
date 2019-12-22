import pytest
from leetcode import find_number


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([12, 345, 2, 6, 7896], 2),
        ([555, 901, 482, 1771], 1),
    ],
)
def test_find_number(nums, expected):
    assert find_number.find_numbers(nums) == expected
