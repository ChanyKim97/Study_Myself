def sum_digits(n):
    # if n//10 == 0 and n%10 == 0:
    #     return 0
    # digit = n%10
    # return sum_digits(n//10) + digit
    if n<10:
        return n
    return n%10 + sum_digits(n//10)


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))