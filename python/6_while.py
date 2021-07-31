# i=1
# while i<=3:
#     print("나는 잘생겼다.")
#     i+=1
#
# i=0
# while i <= 100:
#     i += 8
#     if i % 12 == 0:
#         i = i
#     else:
#         print(i)


i = 1
sum = 0

while i<1000:
    if i%2 == 0:
        sum += i
    if i%3 == 0:
        sum += i
    if i%6 == 0:
        sum -= i
    i += 1

print(sum)