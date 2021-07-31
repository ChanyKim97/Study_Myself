from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        randomnum = randint(0, 9)
        if randomnum not in numbers:
            numbers.append(randomnum)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers



def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []

    while len(new_guess) < 3:
        guess = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요: "))

        if guess < 0 or guess >9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        new_guess.append(guess)

    return new_guess



def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] in solution:
            if guess[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1
        else:
            continue

    return strike_count, ball_count



ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1
    guess = take_guess()
    s, b = get_score(guess, ANSWER)
    print(f"{s}S {b}B\n")
    if s == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))