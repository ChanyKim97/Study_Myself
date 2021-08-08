# def power(x, y):
#     total = 1
#
#     # x를 y번 곱해 준다
#     for i in range(y):
#         total *= x
#
#     return total

#위 알고리즘의 시간복잡도는 O(y)
#O(logy)로

def power(x, y):
    #base case
    if y == 0:
        return 1

    if y%2 == 0:
        return power(x, y//2) * power(x, y//2)
    else:
        return x * power(x, y//2) * power(x, y//2)





# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))