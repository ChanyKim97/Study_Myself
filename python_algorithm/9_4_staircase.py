def staircase(stairs, possible_steps):
    if stairs < 0:
        return 0
    if stairs < 2:
        return 1

    allsum = 0

    for i in possible_steps:
        allsum += staircase(stairs-i, possible_steps)

    return allsum



print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))