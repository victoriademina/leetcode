def sort_array_by_parity(nums):
    new_list = []
    for i in nums:
        if i % 2 == 0:
            new_list.append(i)
    for i in nums:
        if i % 2 != 0:
            new_list.append(i)
    return new_list
