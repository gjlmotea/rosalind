s = "GATATATGCATATACTT"
sub = "ATAT"

positions = []

for i in range(0, len(s) - len(sub) + 1):
    match = True
    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break
    if match:
        positions.append(i + 1)

for m in positions:
    print(m, end=" ")
