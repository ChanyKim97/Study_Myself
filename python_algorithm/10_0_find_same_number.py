def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list)

    if start >= end:
        return start

    mid = (start + end) // 2

    low_than_mid = 0

    for i in some_list:
        if start<= i and i <= mid:
            low_than_mid += 1

    if low_than_mid > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid+1, end)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))