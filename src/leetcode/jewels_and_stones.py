"""
https://leetcode.com/problems/jewels-and-stones/
"""


def jewels_and_stones(j, s):
    count = 0
    for i in j:
        for x in s:
            if i == x:
                count = count + 1
    return count
