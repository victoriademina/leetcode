import pytest
from leetcode import height_checker


@pytest.mark.parametrize(
    'heights,expected',
    [
        ([1, 1, 4, 2, 1, 3], 3),
        ([5, 1, 2, 3, 4], 5),

    ],
)
def test_height_checker(heights, expected):
    assert height_checker.height_checker(heights) == expected
