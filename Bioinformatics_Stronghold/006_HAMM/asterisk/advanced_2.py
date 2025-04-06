# item, cost 只能用位置參數。剩下傳入的位置參數都會被*extra收集起成tuple
def record_1(item, cost, /, *extra):
    print(item, cost, extra)  # 早餐 $50 ('便利商店', '一杯咖啡、兩顆茶葉蛋')
    print(*extra)  # 早餐 $50 ('便利商店', '一杯咖啡、兩顆茶葉蛋')

record_1("早餐", "$50", "便利商店", "一杯咖啡、兩顆茶葉蛋")

# item, cost 只能用具名參數。剩下傳入的具名參數都會被**extra收集成dict
def record_2(*, item, cost, **extra):
    print(item, cost, extra)  # 晚餐 $120 {'地點': '火鍋店', '備註': '原味健康火鍋'}
    print(*extra) # 地點 備註 => 印出key
    # print(**extra)  # 會報錯 => print()不支援印出具名參數

record_2(item="晚餐", cost="$120", 地點="火鍋店", 備註="原味健康火鍋")
