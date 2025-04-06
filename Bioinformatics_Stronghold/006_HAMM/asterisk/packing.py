# ==== single star ====
def add_all(*args):  # 收參數（打包），把傳進來的位置參數放進tuple中
    print(*args)  # 1 2 3 4 => 解參數、解包後的樣子
    print(args)  # (1, 2, 3, 4) => 未解包的模樣
    print(args[0])  # 1

    return sum(args)

total = add_all(1, 2, 3, 4)
print(total)  # 10

# ==== double star ====
def parse_data(**kwargs):  # 允許無限制數量的關鍵字參數
    for name, cost in kwargs.items():
        print(name, cost)

record = {'早餐': '$35', '午餐': '$80'}

parse_data(**record)
# 早餐 $35
# 午餐 $80

parse_data(午餐='$50', 晚餐='$30', 宵夜='$250')  # 支援跟鬼一樣的用法
# 午餐 $50
# 晚餐 $30
# 宵夜 $250
