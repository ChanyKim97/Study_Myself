# name = input("이름을 입력하세요: ")
#
# #input함수는 항상 문자열로 받아옴
#
# print(name)
#
import random

# 코드를 작성하세요.
randnum = random.randint(1, 20)
i = 0
while i < 4:
    usernum = int(input(f"기회가 {4 - i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if usernum == randnum:
        print(f"축하합니다. {1 + i}번 만에 숫자를 맞히셨습니다.")
        break
    else:
        if usernum < randnum:
            print("Up")
        else:
            print("Down")
    i += 1
    if i == 4:
        print(f"아쉽습니다. 정답은 {randnum}입니다.")
