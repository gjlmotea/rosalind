def born_recur(n: int, m: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n <= m:
        # 還沒有死亡，等同於經典 Fibonacci
        return born_recur(n - 1, m) + born_recur(n - 2, m)


    # 以下可以簡寫成這行
    # return sum(born_recur(n - i, m) for i in range(2, m + 1))
    total = 0
    for i in range(2, m + 1):         # 計算 n-2, n-3, …, n-m 月時
        total += born_recur(n - i, m) # 那些月份的兔子在本月各生一對
    return total

print(born_recur(6, 3))  # 4
# 遞迴算法較慢


# 或者以下寫法，計算新生兔子數量

# # 計算第n回合出生的新兔數
# def births(n: int, m: int) -> int:
#     if n <= 0:
#         return 0  # 尚未進入回合
#     if n == 1:
#         return 1  # 第1回合初始條件 => 題目給定有1對新生兔
#     if n == 2:
#         return 0  # 第2回合，初代兔剛成熟，下回合才開始繁殖 ⇒ 本回合無新生
#
#     # 第3回合起：新生數 = 所有成熟兔（滿2回合以上且尚未死亡）各生 1 對
#     return sum(births(n - i, m) for i in range(2, m + 1))
#
# # 計算第n回合仍存活的兔子總數
# def alive(n: int, m: int) -> int:
#     if n <= 0: return 0
#     # 活著 = 最近m個月內出生者
#     return sum(births(n - i, m) for i in range(0, m))
#
# print(alive(6, 3))  # 4
