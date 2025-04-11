import math

k, m, n = 2, 2, 2
total = math.comb(k + m + n, 2)
kk = math.comb(k, 2)
mm = math.comb(m, 2)
nn = math.comb(n, 2)

print((kk * 1 + mm * 0.75 + nn * 0 + k * m * 1 + k * n * 1 + m * n * 0.5) / total)
