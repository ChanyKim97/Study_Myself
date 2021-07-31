from random import randint

def generate_numbers(n):
    lotto_correct = []

    while len(lotto_correct) < n:
        num = randint(1,45)
        if num not in lotto_correct:
            lotto_correct.append(num)

    return lotto_correct

# print(generate_numbers(6))

# def draw_winning_numbers():
#     general_num = generate_numbers(6)
#     general_num.sort()
#
#     while True:
#         bonus_num = generate_numbers(1)
#         if bonus_num[0] not in general_num:
#             general_num.append(bonus_num[0])
#             break
#
#     return general_num
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(list_1, list_2):
    # count = 0
    # for i in range(len(list_1)):
    #     for j in range(len(list_2)):
    #         if list_1[i] == list_2[j]:
    #             count += 1
    # return count
    count = 0
    for num in list_1:
        if num in list_2:
            count += 1
    return count


def check(numbers, winning_numbers):
    general_correct_count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers,winning_numbers[6:])

    if general_correct_count == 6:
        return 1000000000
    elif general_correct_count == 5:
        if bonus_count == 1:
            return 50000000
        else:
            return 1000000
    elif general_correct_count == 4:
        return 50000
    elif general_correct_count == 3:
        return 5000
    else:
        return 0


# print(draw_winning_numbers())
#print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
#numbers_test = [2, 4, 11, 14, 25, 40]
#winning_numbers_test = [2, 4, 10, 11, 14, 40, 25]

#print(check(numbers_test, winning_numbers_test))