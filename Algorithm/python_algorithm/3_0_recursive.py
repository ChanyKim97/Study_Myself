def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

print(factorial(4))

#반복문은 재귀로 항상 풀수 있음
#재귀에는 치명적인 단점이 있음 call stack이 많이 쌓이게 되면 error

