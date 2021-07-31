temperature = 16

if temperature <= 10:
    print("자켓을 입는다")
else:
    print("자켓을 입지않는다")

    i = 0
    while i <= 100:
        i += 8
        if i % 12 == 0:
            i = i
        else:
            print(i)