import pytest
from leetcode import next_greater_element


@pytest.mark.parametrize(
    'nums1,nums2,expected',
    [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ],
)
def next_greater_element(nums1, nums2, expected):
    assert next_greater_element.next_greater_element(nums1, nums2) == expected
