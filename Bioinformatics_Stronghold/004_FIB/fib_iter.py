def rabbit_population(n, k):
    R, r = 0, 1  # R: 成熟兔數量、r: 初生兔數量
    for _ in range(1, n):
        R, r = r, r + k * R
    return r

print(rabbit_population(5, 3))
