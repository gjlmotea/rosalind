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
# print(*seqs.values())
# 原本是一條條的序列
# ATCCAGCT GGGCAACT ATGGATCT AAGCAACC TTGGAACT ATGCCATT ATGGCACT

column = list(zip(*seqs.values())) # nucleotide positions
# 把原本多條序列橫著看了（就可以橫著走天下）
# print(column[0])  # ('A', 'G', 'A', 'A', 'T', 'A', 'A')
# print(column[-1])  # ('T', 'T', 'T', 'C', 'T', 'T', 'T')

# ⚠️*zip vs zip 的差異，在於有沒有「一個個取出」⚠️
# 1. 一個個取出每個元素
# print(list(zip(*seqs.values())))
# [('A', 'G', 'A', 'A', 'T', 'A', 'A'), ('T', 'G', 'T', 'A', 'T', 'T', 'T'), ('C', 'G', 'G', 'G', 'G', 'G', 'G'), ('C', 'C', 'G', 'C', 'G', 'C', 'G'), ('A', 'A', 'A', 'A', 'A', 'C', 'C'), ('G', 'A', 'T', 'A', 'A', 'A', 'A'), ('C', 'C', 'C', 'C', 'C', 'T', 'C'), ('T', 'T', 'T', 'C', 'T', 'T', 'T')]

# 2. 沒有一個個取出，導致變成tuple
# print(list(zip(seqs.values())))
# [('ATCCAGCT',), ('GGGCAACT',), ('ATGGATCT',), ('AAGCAACC',), ('TTGGAACT',), ('ATGCCATT',), ('ATGGCACT',)]

profile = {
    "A": [],
    "C": [],
    "G": [],
    "T": [],
}
consensus = ""

for bases in column:
    nt_counts = {
        "A": bases.count("A"),
        "C": bases.count("C"),
        "G": bases.count("G"),
        "T": bases.count("T"),
    }
    profile["A"].append(nt_counts["A"])
    profile["C"].append(nt_counts["C"])
    profile["G"].append(nt_counts["G"])
    profile["T"].append(nt_counts["T"])

    consensus += max(nt_counts, key=nt_counts.get)

print(consensus)
for base in ["A", "C", "G", "T"]:
    print(base + ":", *profile[base]) # 加入星號解包，避免印出list陣列的`[]`符號
