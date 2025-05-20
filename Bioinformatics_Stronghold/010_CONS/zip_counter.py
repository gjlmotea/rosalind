from collections import Counter

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

def build_profile_and_consensus(sequences: list[str]):
    profile = {nt: [] for nt in "ACGT"}  # => {'A': [], 'C': [], 'G': [], 'T': []}
    consensus = ""

    for column in zip(*sequences):
        nt_counts = Counter(column)

        # print(nt_counts)
        # ex: Counter({'A': 5, 'G': 1, 'T': 1})
        # Counter只記錄有出現的nt，像上面就漏掉了'C'

        for nt in "ACGT":
            profile[nt].append(nt_counts.get(nt, 0)) # 沒出現的base記得要補0，否則會出現None

        most_common = nt_counts.most_common(1) # 取最常出現的前1項1個
        consensus += most_common[0][0] # 只取字母（tuple第0項的第0個元素）
        # 或者 傳遞自訂函數lambda，補0防止key不存在時回傳None
        # consensus += max("ACGT", key=lambda x: nt_counts.get(x, 0))
        # 或者 用__getitem__
        # consensus += max("ACGT", key=nt_counts.__getitem__)

    return consensus, profile

# 測試資料
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

sequences = list(parse_fasta(data).values())
consensus, profile = build_profile_and_consensus(sequences)

print(consensus)
for nt in "ACGT":
    print(f"{nt}: {' '.join(str(x) for x in profile[nt])}")
