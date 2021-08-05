# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = my_list[end]
    biglistindex = start

    for i in range(start, end):
        #요소가 pivot보다 작은경우
        if my_list[i] < pivot:
            swap_elements(my_list, biglistindex, i)
            biglistindex += 1

        #요소가 pivot보다 큰 경우

    swap_elements(my_list, biglistindex, end)
    return biglistindex


# 퀵 정렬
def quicksort(my_list, start, end):
    #base case
    if start >= end:
        return my_list

    pivotindex = partition(my_list,start,end)
    quicksort(my_list, start, pivotindex-1)
    quicksort(my_list, pivotindex+1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)