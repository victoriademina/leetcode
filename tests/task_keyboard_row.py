import pytest
from leetcode import keyboard_row


@pytest.mark.parametrize(
    'words,expected',
    [
        (["Hello", "Alaska", "Dad", "Peace"],
         ["Alaska", "Dad"]),
    ],
)
def test_find_words(words, expected):
    assert keyboard_row.find_words(words) == expected
