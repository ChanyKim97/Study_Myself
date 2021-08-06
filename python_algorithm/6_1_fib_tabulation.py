#tabulation
def fib_tab(n):
    table = [0,1,1]

    for i in range(3, n+1):
        table.append(table[i-1] + table[i-2])

    return table[n]



# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))