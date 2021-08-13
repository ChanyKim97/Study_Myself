def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return

    midindex = (start_index + end_index) // 2

    if some_list[midindex] == element:
        return midindex
    elif element > some_list[midindex]:
        return binary_search(element, some_list, midindex+1)
    else:
        return binary_search(element,some_list, start_index, midindex-1)
    # elif some_list[midindex] > element:
    #     return binary_search(element, some_list, start_index, midindex)
    # else:
    #     return binary_search(element, some_list, midindex+1, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))