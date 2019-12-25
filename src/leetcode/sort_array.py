def sort_array(n):
    list_odd = []
    list_even = []
    result = []
    for i in n:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    zipped = zip(list_even, list_odd)
    for first, second in zipped:
        result.append(first)
        result.append(second)
    return result
