names = ['早餐', '午餐', '晚餐']
costs = ['$35', '$80', '$65']

zipped = list(zip(names, costs))  # 由3個tuple組成的list
print("記錄：", zipped)  # [('早餐', '$35'), ('午餐', '$80'), ('晚餐', '$65')]

# 拆解方式1：拆包 多變數賦值／序列解包
record_1, record_2, record_3 = zipped
print(record_1)  # ('早餐', '$35')
print(record_2)  # ('午餐', '$80')
print(record_3)  # ('晚餐', '$65')

# 拆解方式2：解包 轉置解包／參數解包
names, costs = zip(*zipped)
print(names)  # ('早餐', '午餐', '晚餐')
print(costs)  # ('$35', '$80', '$65')
