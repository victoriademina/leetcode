import pytest
from leetcode import valid_anagram


@pytest.mark.parametrize(
    's,t,expected',
    [
        ("anagram", "nagaram", True),
        ("cats", "dogs", False),
    ],
)
def valid_anagram(s, t, expected):
    assert valid_anagram.valid_anagram(s, t) == expected
