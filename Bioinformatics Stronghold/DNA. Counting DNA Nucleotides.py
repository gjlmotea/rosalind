s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(len(s)):
    match s[i]:
        case 'A':
            counts['A'] += 1
        case 'C':
            counts['C'] += 1
        case 'G':
            counts['G'] += 1
        case 'T':
            counts['T'] += 1

print(" ".join(str(counts[key]) for key in counts)) # 去掉最後一個空白字符
# print(counts['A'], counts['C'], counts['G'], counts['T'])