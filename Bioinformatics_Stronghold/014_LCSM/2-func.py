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

def longest_common_substring(seqs: dict) -> str:
    s_seq = min(seqs.values(), key=len)
    n = len(s_seq)

    for L in range(n, 0, -1):
        for i in range(n - L + 1):
            candidate = s_seq[i:i+L]
            if all(candidate in seq for seq in seqs.values()):
                return candidate

data = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

seqs = parse_fasta(data)
print(longest_common_substring(seqs))
