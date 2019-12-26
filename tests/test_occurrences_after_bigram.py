import pytest
from leetcode import occurrences_after_bigram


@pytest.mark.parametrize(
    'text,first,second,expected',
    [
        ("alice is a good girl she is a good student", "a", "good", ["girl", "student"]),
        ("we will we will rock you", "we", "will", ["we", "rock"]),
    ],
)
def test_jewels_and_stones(text, first, second, expected):
    assert occurrences_after_bigram.find_occurrences(text, first, second) == expected
