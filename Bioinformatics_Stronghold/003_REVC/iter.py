s = "AAAACCCGGT"

rev_s = s[::-1]
# 或者
# rev_s = ''.join(reversed(s))

for base in rev_s:
    match base:
        case 'A':
            print('T', end='')
        case 'C':
            print('G', end='')
        case 'G':
            print('C', end='')
        case 'T':
            print('A', end='')