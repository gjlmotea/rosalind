# 一般寫法
def record_item(item: str, cost: str):
    print(item, cost)

record_item("早餐", "$10")  # 位置參數，按照順序填
record_item(item="午餐", cost="$120")  # 具名參數，指定關鍵字

# 強制使用具名參數 => 在*右側的參數，只能用具名參數(keyword)
def record_item_k1(*, item: str, cost: str):
    print(item, cost)

# record_item_k1("早餐", "$10") => 會出錯，不能用"位置參數"
record_item_k1(item="午餐", cost="$120")

def record_item_k2(item: str, *, cost: str): # *在中間 => 只有*右側的cost需要使用具名參數
    print(item, cost)

record_item_k2(item="午餐", cost="$120")
record_item_k2("晚餐", cost="$250") # 這行可運作

# 強制使用位置參數 => 在/左側的參數，只能用位置參數(positional)
def record_item_p1(item: str, cost: str, /):
    print(item, cost)

# record_item_p1(item="午餐", cost="$120") # 會出錯，不能用"具名參數"
record_item_p1("晚餐", "$250") # 這行可運作

# 兩者混用mix（強制具名、強制位置）
# 若兩同時存在，/必須出現在*前面
def record_item_m1(item: str, /, cost: str, *, notes: str):
    print(item, cost)

record_item_m1("蹦迪", "$1000", notes="好貴")

# def record_item_m2(item: str, *, cost: str, /): # 這行會報錯 SyntaxError: / must be ahead of *
#     print(item, cost)
