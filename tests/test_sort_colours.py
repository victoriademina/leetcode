import pytest
from leetcode import sort_colours


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([0, 1, 2, 1, 2], [0, 1, 1, 2, 2]),
        ([1, 2, 1], [1, 1, 2]),
        ([1], [1]),
    ],
)
def test_sort_colours(nums, expected):
    assert sort_colours.sort_colours(nums) == expected
