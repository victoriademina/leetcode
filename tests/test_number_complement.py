import pytest
from leetcode import number_complement


@pytest.mark.parametrize(
    'num,expected',
    [
        (5, 2),
        (1, 0),
    ],
)
def test_number_complement(num, expected):
    assert number_complement.find_complement(num) == expected
