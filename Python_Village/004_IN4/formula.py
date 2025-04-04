a, b = 100, 200

# 如果a, b是偶數，則調整為奇數
if a % 2 == 0:
    a += 1
if b % 2 == 0:
    b -= 1

# 也可這樣寫，如果a是偶數則+1；如果b是偶數，則-1
# a += a % 2 == 0
# b -= b % 2 == 0

n = (b - a) // 2 + 1 # 奇數項數
total = n * (a + b) // 2

print(total)
