"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""


def find_numbers(nums):
    result = 0
    for i in nums:
        i = str(i)
        if len(i) % 2 == 0:
            result = result + 1
    return result
