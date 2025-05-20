data = """
	>Rosalind_1
	ATCCAGCT
	>Rosalind_2
	GGGCAACT
	>Rosalind_3
	ATGGATCT
	>Rosalind_4
	AAGCAACC
	>Rosalind_5
	TTGGAACT
	>Rosalind_6
	ATGCCATT
	>Rosalind_7
	ATGGCACT
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
profile_width = len(next(iter(seqs.values())))  # 取出seqs.values()中第一條序列的長度

# profile matrix 使用二維陣列來記錄
profile = [
    # [0, 0, 0, 0, 0, 0, 0, 0],  # A
    # [0, 0, 0, 0, 0, 0, 0, 0],  # C
    # [0, 0, 0, 0, 0, 0, 0, 0],  # G
    # [0, 0, 0, 0, 0, 0, 0, 0],  # T
    [0] * profile_width
    for i in range(4)  # 自動化產相對應的長度
]

for seq in seqs.values():
    for i in range(len(seq)):
        match seq[i]:
            case "A":
                profile[0][i] += 1
            case "C":
                profile[1][i] += 1
            case "G":
                profile[2][i] += 1
            case "T":
                profile[3][i] += 1

# print(profile)
# [[5, 1, 0, 0, 5, 5, 0, 0], [0, 0, 1, 4, 2, 0, 6, 1], [1, 1, 6, 3, 0, 1, 0, 0], [1, 5, 0, 0, 0, 1, 1, 6]]

consensus = ""  # 中文翻譯為"共識"。共識字串：在每個位置上「出現最多次的字母（鹼基）／最多序列相同」 組成的字串
nucleotides = ["A", "C", "G", "T"]

for i in range(profile_width):
    nt_counts = [profile[0][i], profile[1][i], profile[2][i], profile[3][i]]
    max_index = nt_counts.index(max(nt_counts))
    consensus += nucleotides[max_index]  # 0,1,2,3 => A,C,G,T

print(consensus)
for i, counts in enumerate(profile):
    print(nucleotides[i] + ":", *counts)
