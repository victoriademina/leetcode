"""
https://leetcode.com/problems/robot-return-to-origin/
"""


def return_to_origin(moves):
    new_moves = [0, 0]
    for i in moves:
        if i == "R":
            new_moves[0] = new_moves[0] + 1
        elif i == "L":
            new_moves[0] = new_moves[0] - 1
        elif i == "U":
            new_moves[1] = new_moves[1] + 1
        else:
            new_moves[1] = new_moves[1] - 1
    if new_moves == [0, 0]:
        return True
    else:
        return False
