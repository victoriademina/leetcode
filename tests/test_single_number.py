import pytest
from leetcode import single_number


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([2, 2, 1], 1),
        ([1, 2, 1], 2),
        ([1], 1),
    ],
)
def test_single_number(nums, expected):
    assert single_number.single_number(nums) == expected
