## ==== min, max 用法研究 ====

## max(), min()
data = [1, 2, 3, 100, 50, 50]
print(min(data))  # 100
print(max(data))  # 1

## default用法
data = [] # default僅在「iterable為空」時有用。ex: data={}, (), set(), ""
print(min(data, default=9999))  # 9999
print(min(data, default=float("inf")))  # inf
print(max(data, default=0))  # 0
print(max(data, default=float("-inf")))  # -inf


## key用法：count
data = [1, 2, 3, 100, 50, 50]
print(data.count(100)) # 1 -> 100出現了1次
print(data.count(50)) # 2 -> 50出現了2次

for i in set(data):  # 用set移除重複
    print(f"{i} 出現了 {data.count(i)} 次")
    # 1 出現了 1 次
    # 2 出現了 1 次
    # 3 出現了 1 次
    # 100 出現了 1 次
    # 50 出現了 2 次

most_frequent_value = max(set(data), key=data.count)
most_frequent_count = data.count(most_frequent_value)

print(most_frequent_value)  # 50
print(most_frequent_count)  # 2


## key用法：len
data = ["apple", "book", "cat", "dog"]
print(len(data[1])) # 4

for i in data:
    print(f"{i} 長度為 {len(i)}")

longest_item = max(data, key=len)
longest_length = len(longest_item)

print(longest_item) # apple
print(longest_length) # 5


## key用法：dict字典（key-value）
data = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 90,
    "Diana": 60,
}

print(max(data))  # Diana -> 挑出key字母順序最大者
print(max(data.keys()))  # Diana -> 同上，dict迭代預設就是keys()
print(max(data.values()))  # 95 -> 挑出最高分（value最大）

# ⚠️這幾種方法，要嘛挑出key（捨棄value的資訊）、要嘛挑出value（捨棄key的資訊）
# 無法得知value是哪個 key
# 需要反查dict，才能從「最高分」反推出「學生」


## key用法：dict.get字典查值（同時保留 key 與 value 資訊）
data = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 90,
    "Diana": 60,
}

for i in data:
    print(f"{i} 的分數是 {data.get(i)}")
    # Alice 的分數是 88
    # Bob 的分數是 95
    # Charlie 的分數是 90
    # Diana 的分數是 60

highest_scoring_student = max(data, key=data.get)
highest_score = data[highest_scoring_student]

print(highest_scoring_student)  # Bob
print(highest_score)            # 95


words = ["apple", "Banana", "cherry", "Apricot"]

# 按照轉大寫後的字母順序來比大小
print(max(words, key=str.upper))  # cherry
print(min(words, key=str.upper))  # apple
