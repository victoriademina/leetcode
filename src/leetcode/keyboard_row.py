"""
https://leetcode.com/problems/keyboard-row/
"""


def find_words(words):
    first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                 "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    second_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l",
                  "A", "S", "D", "F", "G", "H", "J", "K", "L"]
    third_row = ["z", "x", "c", "v", "b", "n", "m",
                 "Z", "X", "C", "V", "B", "N", "M"]

    result = []

    for w in words:

        count = 0

        for c in w:
            if c in first_row:
                count += 1
        if count == len(w):
            result.append(w)

    for w in words:
        count = 0
        for c in w:
            if c in second_row:
                count += 1
        if count == len(w):
            result.append(w)

    for w in words:
        count = 0
        for c in w:
            if c in third_row:
                count += 1
        if count == len(w):
            result.append(w)

    return result
