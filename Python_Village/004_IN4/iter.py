a, b = 100, 200
total = 0  # 如果用sum作為變數名稱會與內建函數衝突。如果取名為s會誤以為是string縮寫

for i in range(a, b+1):
    if i % 2 == 1:
       total += i

print(total)