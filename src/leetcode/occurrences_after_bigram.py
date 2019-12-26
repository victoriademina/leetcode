"""
https://leetcode.com/problems/occurrences-after-bigram/
"""


def find_occurrences(text, first, second):
    new_list = text.split()
    result = []
    for i in range(len(new_list) - 2):
        if new_list[i] == first and new_list[i + 1] == second:
            result.append(new_list[i + 2])
    return result
