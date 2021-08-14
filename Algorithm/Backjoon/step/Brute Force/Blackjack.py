# N,M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# result = 0
#
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             if arr[i] + arr[j] + arr[k] > M:
#                 continue
#             else:
#                 result = max(result, arr[i] + arr[j] + arr[k])
#
#
# print(result)
#순열 사용
from itertools import combinations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

#이렇게 3 붙이면 순열로 3개의 원소로 구성된 수열을 만들어줌
for card in combinations(arr, 3):
    temp_result = sum(card)
    if result < temp_result <= M:
        result = temp_result

print(result)