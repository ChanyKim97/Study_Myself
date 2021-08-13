def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list)

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if element == some_list[mid_index]:
            return mid_index
        elif element > some_list[mid_index]:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
#   if element not in some_list: 알고리즘에 매우 안좋음 'in'
#      return None

#    midindex = len(some_list) // 2

#   if some_list[midindex] == element:
#       return midindex
#   else:
#       if element > some_list[midindex]:
#            binary_search(element, some_list[midindex+1:])
#        else:
#            binary_search(element, some_list[:midindex])
# 이러면 안됨




print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))