# ==== single star ====
args = (1, 2, 3, 4)
print(*args)  # 解開成 1 2 3 4

list1 = [1, 2, 3]
list2 = [4, 5]
combined = [*list1, *list2]  # 解開陣列，存入新陣列中
print(combined)  # [1, 2, 3, 4, 5]

zipped = [('早餐', '$35'), ('午餐', '$80'), ('晚餐', '$65')]
record_1, *others = zipped # 把右邊拆開放到左邊
print(record_1)  # ('早餐', '$35')
print(others) # [('午餐', '$80'), ('晚餐', '$65')]

# ==== double star ====
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3}
merged = {**dict1, **dict2}  # 解開字典，存入新字典中
print(merged)  # {'a': 1, 'b': 2, 'c': 3}
