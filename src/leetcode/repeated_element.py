def repeated_element(nums):
    new_list = []
    for i in nums:
        if i in new_list:
            return i
        else:
            new_list.append(i)
