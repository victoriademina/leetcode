import pytest
from leetcode import contains_duplicate


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 2, 3, 4, 4, 5], True),
        ([1, 2, 3, 4, 5, 8], False),
    ],
)
def contains_duplicates(nums, expected):
    assert contains_duplicate.contains_duplicate(nums) == expected
