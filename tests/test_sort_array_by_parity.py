import pytest
from leetcode import sort_array_by_parity


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([3, 1, 2, 4], [2, 4, 3, 1]),
    ],
)
def test_sort_array_by_parity(nums, expected):
    assert sort_array_by_parity.sort_array_by_parity(nums) == expected
