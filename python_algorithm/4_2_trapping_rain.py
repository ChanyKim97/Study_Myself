#빌딩 사이의 물 채우기 양 구하기
def trapping_rain(buildings):
    trapping_amount = 0

    #1번 index와 마지막 index는 물이 채워질수가 없음
    for i in range(1,len(buildings) - 1):
        #leftmost
        #leftmost = 0
        #for j in range(i):
        #    leftmost = max(leftmost, buildings[j])
        leftmost = max(buildings[:i])

        #rightmost = 0
        #for k in range(i+1, len(buildings)):
        #    rightmost = max(rightmost, buildings[k])
        rightmost = max(buildings[i:])

        if buildings[i] <= leftmost and buildings[i] <= rightmost:
            trapping_amount += min(leftmost, rightmost) - buildings[i]
        else:
            continue

    return trapping_amount




print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))