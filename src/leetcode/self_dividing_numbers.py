"""
https://leetcode.com/problems/self-dividing-numbers/
"""


def self_dividing_numbers(left, right):
    new_list = []
    for i in range(left, right + 1):
        str_i = str(i)
        count = 0
        for x in str_i:
            int_x = int(x)
            if int_x != 0:
                if i % int_x == 0:
                    count = count + 1
            else:
                break
        if count == len(str_i):
            new_list.append(i)
    return new_list
