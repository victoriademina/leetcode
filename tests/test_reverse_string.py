import pytest
from leetcode import reverse_string


@pytest.mark.parametrize(
    's,expected',
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),

    ],
)
def test_reverse_string(s, expected):
    reverse_string.reverse_string(s)
    assert s == expected
