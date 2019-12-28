import pytest
from leetcode import uncommon_words


@pytest.mark.parametrize(
    'a,b,expected',
    [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("apple apple", "banana", ["banana"]),
    ],
)
def test_uncommon_words(a, b, expected):
    assert uncommon_words.uncommon_words(a, b) == expected
