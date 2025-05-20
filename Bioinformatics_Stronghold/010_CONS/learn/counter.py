## ==== collections.Counter 用法研究 ====

from collections import Counter

# 範例一：字串
c = Counter("AAGCAACC")
print(c)  # Counter({'A': 4, 'C': 3, 'G': 1}) 依出現次數高到低排序

print(
    c["A"]
)  # 4 -> 等價寫法 print(c.__getitem__("A")) 👉索引取值`[]`的寫法就是__getitem__函式語法糖
print(c.get("A"))  # 4

print(c["T"])  # 0 -> 查不到 "T"
print(c.get("T"))  # None -> 查不到 "T"⚠️小心出現None！

# 取出現次數最多的前n項、以及出現次數
print(c.most_common(1))  # [('A', 4)]
print(c.most_common(2))  # [('A', 4), ('C', 3)]


# 範例二：list串列
c = Counter(["", " ", "a", "a", "b", "c", "c", "c"])
print(c)  # Counter({'c': 3, 'a': 2, '': 1, ' ': 1, 'b': 1})
print(sum(c.values()))  # 總元素數: 8


# 範例三：dict字典（Counter本質上就是dict）
# 倒推還原，由統計資料導回原本的元素內容
c = Counter({"A": 4, "C": 3, "G": 1})  # dict只能帶入int數字
print(c)  # Counter({'A': 4, 'C': 3, 'G': 1})

print(list(c.elements()))  # ['A', 'A', 'A', 'A', 'C', 'C', 'C', 'G']


# 範例四：集合運算
c = Counter({"A": 4, "C": 3, "G": 1})
d = Counter({"A": 1, "C": 10})

print(c + d) # Counter({'C': 13, 'A': 5, 'G': 1}) 加法
print(c - d) # Counter({'A': 3, 'G': 1}) 減法。負值、零值會被過濾掉
print(c & d) # Counter({'C': 3, 'A': 1}) 交集（取min）
print(c | d) # Counter({'C': 10, 'A': 4, 'G': 1}) 聯集（取max）

c.subtract(d) # 原地減法(in-place subtraction)，會保留負值、零值
print(c) # Counter({'A': 3, 'G': 1, 'C': -7})