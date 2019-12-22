import pytest
from leetcode import product_and_sum


@pytest.mark.parametrize(
    'n,expected',
    [
        (234, 15),
        (4421, 21),
    ],
)
def test_product_and_sum(n, expected):
    assert product_and_sum.subtract_product_and_sum(n) == expected
