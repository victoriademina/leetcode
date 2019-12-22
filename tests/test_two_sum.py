import pytest
from leetcode import two_sum


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum.two_sum(nums, target) == expected
