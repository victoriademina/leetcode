"""
https://leetcode.com/problems/array-partition-i/submissions/
"""


def array_partition(nums):
    new_list = sorted(nums)
    min_list = []
    for i in range(0, len(new_list), 2):
        min_list.append(new_list[i])
    return sum(min_list)
