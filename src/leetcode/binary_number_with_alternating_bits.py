"""
https://leetcode.com/problems/binary-number-with-alternating-bits/
"""


def binary_number(n):
    bits = bin(n)
    count = 0
    for x in range(len(bits) - 1):
        if bits[x] == bits[x + 1]:
            count = count + 1
    if count > 0:
        return False
    else:
        return True
