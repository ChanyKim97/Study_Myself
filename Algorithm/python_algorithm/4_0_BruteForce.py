def max_product(left_cards, right_cards):
    max = 0
    for i in left_cards:
        for j in right_cards:
            if i*j > max:
                max = i*j

    return max
#모든 경우 찾아보지만 인풋이 큰경우에대해 효율적이지 못함
#직관적이고 명확하지만 단점이 명확함


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))