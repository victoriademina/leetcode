"""
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums, target):
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i + 1:]):
            if n + m == target:
                return [i, j + i + 1]
