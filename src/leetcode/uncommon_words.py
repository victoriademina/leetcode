import collections


def uncommon_words(A, B):
    new_a = A.split()
    new_b = B.split()

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
