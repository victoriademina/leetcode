import pytest
from leetcode import sort_array


@pytest.mark.parametrize(
    'n,expected',
    [
        ([4, 2, 5, 7], [4, 5, 2, 7]),

    ],
)
def test_sort_array(n, expected):
    assert sort_array.sort_array(n) == expected
