"""
https://leetcode.com/problems/height-checker/
"""


def height_checker(heights):
    new_list = sorted(heights)
    count = 0
    for i in range(len(new_list)):
        if heights[i] != new_list[i]:
            count += 1
    return count
