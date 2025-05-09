# 一開始寫 step1
def build_table_step1(t):
    table = [0]  # 先建好第0項 失敗表[0]
    length = 0  # 目前位置的 最長(前綴=後綴)的長度，是失敗表所填入的數字
    for i in range(1, len(t)):  # 從第2項（索引為1)開始比對
        if t[i] == t[length]:  # 若兩者合得來，combo數+1
            length += 1
            table.append(length)
        else:
            length = 0  # => 寫法錯誤，但先這樣試試
            table.append(length)
    return table


# １號練習題
print(build_table_step1("AABBABABBA"))  # [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

# ２號練習題：
print(build_table_step1("AABAABBAAA"))  # [0, 1, 0, 1, 2, 3, 0, 1, 2, 0(*)]


# 接著到 step2
def build_table_step2(t):
    table = [0]
    length = 0
    for i in range(1, len(t)):
        if t[i] == t[length]:
            length += 1
            table.append(length)
        else:
            # length = table[i - 1]  # => 寫法錯誤：改成延續「前一項數值」，其實不對
            length = table[length - 1] # => 改成這樣會更接近一點，回退、跳到上一個紀錄資訊（存檔點）=> 但也還不對
            table.append(length)
    return table


# １號練習題
print(build_table_step2("AABBABABBA"))  # [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

# ２號練習題：
print(build_table_step2("AABAABBAAA"))  # [0, 1, 0, 1, 2, 3, 0, 1, 2, 1(*)]



# 接著到 step3
def build_table_step3(t):
    table = [0]
    length = 0
    for i in range(1, len(t)):
        # 失戀就找上一任女友，直到合得來 or 恢復單身
        while length > 0 and t[i] != t[length]:
            length = table[length - 1]

        # 哇，下一個對象是我合的來的人，直接變女友
        if t[i] == t[length]:
            length += 1
        # 原本else處程式碼，已改寫成上面的while邏輯了

        table.append(length)
    return table

# １號練習題
print(build_table_step3("AABBABABBA"))  # [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

# ２號練習題：
print(build_table_step3("AABAABBAAA"))  # [0, 1, 0, 1, 2, 3, 0, 1, 2, 2]

# ３號練習題：
print(build_table_step3("AAABAAAAAB"))  # [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]


# 主程式 step1
def kmp_search_step1(s, t):
    positions = []
    table = build_table_step3(t) # 建立失敗表
    length = 0
    for i in range(len(s)): # 不是從1開始喔，而是也須要比對[0]
        # for j in range(len(t)): # 不是這種雙迴圈的寫法喔！
        #    ...

        if s[i] == t[length]: # 字元比對成功
            length += 1
        # else: # 1. 字元比對失敗，這裡要做什麼？
            # ???
        if length == len(t): # 字串完全匹配
            positions.append(i) # 2. 錯誤寫法，底下length也不該歸0
            length = 0

    return positions


s = "GATATATGCATATACTT"
sub = "ATAT"

print(kmp_search_step1(s, sub)) # [4, 10, 15] 錯誤 => 正確答案是 [2, 4, 10]



# 主程式 step2
def kmp_search_step2(s, t):
    positions = []
    table = build_table_step3(t)
    length = 0
    for i in range(len(s)):
        while length > 0 and s[i] != t[length]:
            length = table[length - 1]
        if s[i] == t[length]: # 字元比對成功
            length += 1
        # 原本else處程式碼，已改寫成上面的while邏輯了

        if length == len(t): # 字串完全匹配
            positions.append(i - length +2) # 起點位置：i - length + 1，且index預設為0，需再+1
            length = table[length - 1] # 匹配完重設回前一個 ex: 主字串：AAAA、子字串：AA

    return positions


s = "GATATATGCATATACTT"
sub = "ATAT"

print(kmp_search_step2(s, sub)) # [2, 4, 10]