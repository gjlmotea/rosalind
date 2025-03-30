def reverse_complement(s):
    # 先互補（替換），再反轉
    trans_table = str.maketrans('ATCG', 'TAGC')
    rev_s = s.translate(trans_table)
    return rev_s[::-1]

s = "AAAACCCGGT"
print(reverse_complement(s))
