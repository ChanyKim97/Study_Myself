def sublist_max(profits):
    maxx = profits[0]
    innermaxx = profits[0]

    for i in range(1, len(profits)):
        innermaxx = max(innermaxx + profits[i], profits[i])

        maxx = max(maxx, innermaxx)

    return maxx



# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))