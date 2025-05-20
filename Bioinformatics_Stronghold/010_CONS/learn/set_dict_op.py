## ==== set、dict 能做的運算 ====

# set 可以做交集、聯集、差集
c = {"A", "C", "G"}
d = {"A", "C", "G", "T"}
print(c & d) # {'C', 'G', 'A'} （交集and運算）
print(c | d) # {'C', 'T', 'G', 'A'}（聯集or運算）
print(c - d) # set() 被減光了（差集diff運算）
print(c ^ d) # {'T'}（異或xor運算）


# dict 只能做 合併字典
c = {"A": 4, "C": 3, "G": 1}
d = {"A": 1, "C": 10}

print(c | d) # {'A': 1, 'C': 10, 'G': 1}
# dict union 有相同元素時，右邊會覆蓋左邊

e = {**c, **d} # 合併字典（倒出元素到新dict）
print(e) # {'A': 1, 'C': 10, 'G': 1}

c.update(d) # 合併（更新）字典
print(c) # {'A': 1, 'C': 10, 'G': 1}
