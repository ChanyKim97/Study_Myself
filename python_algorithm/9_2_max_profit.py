def max_profit(stock_list):
    maxx = stock_list[1] - stock_list[0]
    #현재까지 최대 수익

    minn = min(stock_list[1], stock_list[0])
    #제일 주식이 싼날

    for i in range(2, len(stock_list)):
        maxx = max(maxx, stock_list[i] - minn)

        minn = min(minn, stock_list[i])

    return maxx


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))