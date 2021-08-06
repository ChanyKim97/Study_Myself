def fib_optimized(n):
    current = 1
    previous = 0

    if n < 2:
        return current

    for i in range(2, n+1):
        temp = current
        current += previous
        previous = temp

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
