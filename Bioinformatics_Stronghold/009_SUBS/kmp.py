def kmp_search(s, t):
    positions = []
    table = build_table(t)
    length = 0
    for i in range(len(s)):
        while length > 0 and s[i] != t[length]:
            length = table[length - 1]
        if s[i] == t[length]:  # 字元比對成功
            length += 1

        if length == len(t):  # 字串完全匹配
            positions.append(i - length + 2)  # 起點位置：i - length + 1，且index預設為0，需再+1
            length = table[length - 1]  # 匹配完重設回前一個 ex: 主字串：AAAA、子字串：AA

    return positions

def build_table(t):
    table = [0]
    length = 0
    for i in range(1, len(t)):
        # 失戀就找上一任女友，直到合得來 or 恢復單身
        while length > 0 and t[i] != t[length]:
            length = table[length - 1]

        # 哇，下一個對象是我合的來的人，直接變女友
        if t[i] == t[length]:
            length += 1

        table.append(length)
    return table

s = "GATATATGCATATACTT"
sub = "ATAT"

print(kmp_search(s, sub))
