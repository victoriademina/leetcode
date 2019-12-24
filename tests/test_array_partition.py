import pytest
from leetcode import array_partition


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 4, 3, 2], 4),

    ],
)
def test_array_partition(nums, expected):
    assert array_partition.array_partition(nums) == expected
