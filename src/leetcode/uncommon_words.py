"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""
import collections


def uncommon_words(a, b):
    new_a = a.split()
    new_b = b.split()

    result = []
    counter = collections.Counter()

    for word in new_a:
        counter[word] += 1
    for word in new_b:
        counter[word] += 1

    for word, count in counter.items():
        if count == 1:
            result.append(word)
    return result
