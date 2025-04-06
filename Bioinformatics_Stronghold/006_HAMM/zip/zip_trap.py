# ==== 陷阱1 ====
zipped = zip([1, 2, 3], ['a', 'b', 'c'])
print("陷阱1：", zipped)  # <zip object at 0x12bc43a00> 直接輸出是物件位址
print("陷阱1：", list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print("陷阱1：", list(zipped))  # [] => 空了

# ==== 陷阱2 ====
zipped = zip([1, 2, 3], ['a', 'b', 'c'])
list(zipped)
print("陷阱2：", list(zipped))  # [] => 直接空了

z = list(zipped)  # 要用變數將zip迭代結果存起來，才有辦法重複使用

# ==== 陷阱3 ====
# 長度不一致時，zip 會自動對齊最短長度
# 超出部分會被忽略，而不會報錯
zipped = zip([1, 2, 3], ['a', 'b', 'c', 'd'])  # 因長度不匹配，'d'會被丟掉
print("陷阱3：", list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
