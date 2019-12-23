import pytest
from leetcode import repeated_element


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3, 3], 3),
        ([2, 1, 2, 5, 3, 2], 2),
        ([5, 1, 5, 2, 5, 3, 5, 4], 5)
    ],
)
def test_repeated_element(nums, expected):
    assert repeated_element.repeated_element(nums) == expected
