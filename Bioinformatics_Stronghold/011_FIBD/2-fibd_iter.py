def rabbit_population(n: int, m: int) -> int:
    """
    參數 n (int): 總月數 (共n個回合)

    參數 m (int): 壽命，兔子能活m個月
    """
    if n <= 0 or m <= 0:
        return 0

    r = [1] + [0]*(m-1)
    for _ in range(n-1):
        newborn = sum(r[1:])
        r = [newborn] + r[:-1]
    return sum(r)

print(rabbit_population(6, 3))
# 迭代運算較快