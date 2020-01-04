"""
https://leetcode.com/problems/next-greater-element-i/
"""


def next_greater_element(nums1, nums2):
    result = []
    for n1 in nums1:
        y = find_greater_element(nums2, n1)
        result.append(y)
    return result


def find_greater_element(nums2, n):
    index = 0
    for i in range(len(nums2)):
        if nums2[i] == n:
            index = i
            break
    for x in nums2[index:]:
        if x > n:
            return x
    return -1
