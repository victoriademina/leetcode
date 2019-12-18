import pytest
from leetcode import binary_number_with_alternating_bits


@pytest.mark.parametrize(
    'n,expected',
    [
        (5, True),
        (7, False),
        (11, False),
    ],
)
def test_binary_number(n, expected):
    assert binary_number_with_alternating_bits.binary_number(n) == expected
