def rabbit_population(n, k):
    if n == 1 or n == 2:  # 尚未繁殖，前兩個月都只有一對兔子
        return 1

    # 第n個月兔總數 = 前一個月的兔總數 ＋ 新出生的
    # 新出生的：前一個月成熟兔*k => 前一個月成熟兔數量怎麼計算？就是前兩個月兔總數
    return rabbit_population(n - 1, k) + rabbit_population(n - 2, k) * k


print(rabbit_population(5, 3))
