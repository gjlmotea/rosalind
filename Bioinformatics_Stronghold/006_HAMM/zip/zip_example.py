# ==== 範例1 ====
zipped = zip([1, 2, 3], ['a', 'b', 'c'])
print("範例1：", zipped)  # <zip object at 0x12bc43a00> 直接輸出是物件位址
print("範例1：", list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print("範例1：", list(zipped))  # [] => 空了

# ==== 範例2 ====
student = ['小明', '小華', '小美', '小夫']
score = [85, 92, 78, 88]
subject = ['數學', '數學', '數學', '數學']

class_gradebook = zip(student, score, subject)
# [('小明', 85, '數學'), ('小美', 92, '數學'), ('阿強', 78, '數學'), ('阿珍', 88, '數學')]

for student, score, subject in class_gradebook:
    print("範例2：", student, score, subject)

# 小明 85 數學
# 小美 92 數學
# 阿強 78 數學
# 阿珍 88 數學

