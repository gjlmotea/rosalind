def find_substring_locations(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i + 1)  # 位置從1開始計算位置
    return positions

# 等價的寫法，列表推導式
# def find_substring_locations(s, t):
#     return [
#         i + 1 # 位置從1開始計算位置
#         for i in range(len(s) - len(t) + 1)
#         if s[i:len(t) + i] == t
#     ]

s = "GATATATGCATATACTT"
sub = "ATAT"

print(" ".join(map(str, find_substring_locations(s, sub))))

