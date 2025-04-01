n, k = 5, 3  # n:回合數、k:每次繁衍數

R, r = 0, 1  # R: 成熟兔數量、r: 初生兔數量

for i in range(n - 1):  # 初始狀態已經是第1個月，所以n-1
    new_born = R * k  # 上一輪的成熟兔生小孩了
    R += r  # 上一輪的初生兔子成熟了
    r = new_born

print(R + r)

