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
    length = len(sequences[0])

    # profile matrix 使用dict來記錄
    profile = {
        "A": [0] * length,
        "C": [0] * length,
        "G": [0] * length,
        "T": [0] * length,
    }

    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1

    consensus = ""
    for i in range(length):
        nt_counts = {
            nt: profile[nt][i]
            for nt in "ACGT"
        }
        consensus += max(nt_counts, key=nt_counts.get)

    return consensus, profile

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
