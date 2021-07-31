import random

linecount = 0
englishlist = []
koreanlist = []

with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        voca = line.strip().split(": ")
        english = voca[0]
        korean = voca[1]
        englishlist.append(english)
        koreanlist.append(korean)
        linecount += 1

while True:
    randomindex = random.randint(0, linecount-1)

    guess = input(f"{koreanlist[randomindex]}: ")
    if guess == "q":
        break

    if guess == englishlist[randomindex]:
        print("맞았습니다!")
    else:
        print(f"틀렸습니다. 정답은 {englishlist[randomindex]}입니다.")

