data = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""


def parse_fasta(data: str) -> dict:
    sequences = {}
    label = ""
    for line in data.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            label = line[1:].strip()
            if not label:
                label = ""
                continue
            sequences[label] = ""
        elif label:
            sequences[label] += line

    return sequences


seqs = parse_fasta(data)
s_seq = min(seqs.values(), key=len)  # 找出最短字串作為模板

best = ""  # longest common substring
n = len(s_seq)

# 由長找到短
found = False
for L in range(n, 0, -1):
    for i in range(n-L+1):
        candidate = s_seq[i:i+L]
        if all(candidate in seq for seq in seqs.values()):
            best = candidate
            found = True
            break
    if found:
        break

print(best)
