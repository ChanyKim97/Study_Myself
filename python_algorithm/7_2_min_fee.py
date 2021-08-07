def min_fee(pages_to_print):
    allsum = 0
    eachsum = 0
    for printamount in sorted(pages_to_print):
        eachsum += printamount
        allsum += eachsum

    return allsum


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
