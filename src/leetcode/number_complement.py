"""
https://leetcode.com/problems/number-complement/
"""


def find_complement(num):
    new_num = format(num, "b")
    new_str = ""
    for c in new_num:
        if c == "0":
            new_str += "1"
        elif c == "1":
            new_str += "0"
    return int(new_str, 2)
