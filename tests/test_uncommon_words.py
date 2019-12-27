import pytest
from leetcode import uncommon_words


@pytest.mark.parametrize(
    'A,B,expected',
    [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
    ],
)
def test_uncommon_words(A, B, expected):
    assert uncommon_words.uncommon_words(A, B) == expected
