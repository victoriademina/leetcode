"""
https://leetcode.com/problems/unique-number-of-occurrences/
"""
import collections


def unique_occurrences(arr):
    counter = collections.Counter()
    for i in arr:
        counter[i] += 1
    new_list = []
    for value in counter.values():
        if value not in new_list:
            new_list.append(value)
        else:
            return False
    return True
