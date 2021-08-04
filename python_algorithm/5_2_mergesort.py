def merge(list1, list2):
    list1index = 0
    list2index = 0
    mergelist = []

    while list1index < len(list1) and list2index < len(list2):
        if list1[list1index] > list2[list2index]:
            mergelist.append(list2[list2index])
            list2index += 1
        else:
            mergelist.append(list1[list1index])
            list1index += 1

    if list1index == len(list1):
        mergelist += list2[list2index:]
    else:
        mergelist += list1[list1index:]

    return mergelist



def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    midindex = len(my_list) // 2

    return merge(merge_sort(my_list[:midindex]), merge_sort(my_list[midindex:]))



# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
