def min_coin_count(value, coin_list):
    count = 0
    sort_coin_list = sorted(coin_list, reverse=True)

    for coin in sort_coin_list:
        count += (value // coin)

        value = value % coin

    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))