# 錯誤寫法 例1：看似正常的情況
items = ["a", "", "b", "", "c"]
for item in items:
    if not item:
        items.remove(item)  # 不要這樣做！別在迴圈中修改列表，會造成執行順序錯亂（跳過元素）
print("錯誤寫法 例1：", items)  # ["a", "b", "c"]

# 錯誤寫法 例2：出現非預期的結果
items = ["a", "", "b", "", "", "c"]
for item in items:
    if not item:
        items.remove(item)
print("錯誤寫法 例2：", items)  # ["a", "b", "", "c"]

# 正確寫法（迴圈版）：
items = ["a", "", "b", "", "", "c"]
new_items = []
for item in items:
    if item:  # 只留下真值（篩掉所有falsy值 ex:"", 0, None, False）
        new_items.append(item)
print("正確寫法（迴圈版）：", new_items)  # ['a', 'b', 'c']

# 正確寫法（精簡版）：
items = ["a", "", "b", "", "", "c"]
items = [
    item
    for item in items
    if item
]
# items = [item for item in items if item] # 單行寫法（List Comprehension）
print("正確寫法（精簡版）：", items)  # ['a', 'b', 'c']


# ========
# if (item != "") 只過濾空字串""
# 而 if item 則過濾以下：
# ''       # 空字串
# 0        # 整數零
# 0.0      # 浮點零
# False    # 布林 False
# None     # 空值
# [] {} () 空容器
