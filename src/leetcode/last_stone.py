"""
https://leetcode.com/problems/last-stone-weight/
"""


def last_stone(stones):
    while len(stones) >= 2:
        stones.sort()
        x = stones[-2]
        y = stones[-1]
        if x == y:
            stones = stones[:-2]
        else:
            stones = stones[:-2]
            z = y - x
            stones.append(z)
    if len(stones) > 0:
        return stones[0]
    return 0
