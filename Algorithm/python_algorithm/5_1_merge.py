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


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))