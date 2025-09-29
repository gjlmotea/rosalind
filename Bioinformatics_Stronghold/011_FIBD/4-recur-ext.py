def mortal_fib_recur(n: int, m: int) -> int:
    # 尚未進入回合
    if n <= 0:
        return 0

    # 前兩回合都只有1隻兔子
    if n == 1 or n == 2:
        return 1

    # 還沒有死亡時（從3..m月），等同於經典 Fibonacci
    if n <= m:
        return mortal_fib_recur(n - 1, m) + mortal_fib_recur(n - 2, m)

    # 第一次有兔子死掉（首次死亡月）：m+1月，只扣掉最初那1對
    if n == m + 1:
        return mortal_fib_recur(n - 1, m) + mortal_fib_recur(n - 2, m) - 1

    # 後續死亡月：n > m+1（扣掉 n-m-1 月出生的那批兔子）
    return (mortal_fib_recur(n - 1, m) + mortal_fib_recur(n - 2, m) - mortal_fib_recur(n - m - 1, m))


print(mortal_fib_recur(6, 3))  # 4
