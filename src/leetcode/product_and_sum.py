"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
"""


def subtract_product_and_sum(n):
    n = str(n)
    sum_of_digits = 0
    product_of_digits = 1
    for i in n:
        i = int(i)
        sum_of_digits = sum_of_digits + i
        product_of_digits = product_of_digits * i
    result = product_of_digits - sum_of_digits
    return result
