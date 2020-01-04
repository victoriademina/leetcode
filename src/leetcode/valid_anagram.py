"""
https://leetcode.com/problems/valid-anagram/
"""


def valid_anagram(s, t):
    new_list1 = list(s)
    new_list2 = list(t)
    new_list1.sort()
    new_list2.sort()
    if new_list1 == new_list2:
        return True
    else:
        return False
