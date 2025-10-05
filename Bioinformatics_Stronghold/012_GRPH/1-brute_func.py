from typing import List, Tuple


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



def find_overlap_edges(data: str, k: int = 3) -> List[Tuple[str, str]]:
    seqs = parse_fasta(data)
    edges: List[Tuple[str, str]] = []
    for s1 in seqs:
        for s2 in seqs:
            if s1 == s2:
                continue
            if seqs[s1][-k:] == seqs[s2][:k]:
                edges.append((s1, s2))
    return edges


data = """
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""

for u, v in find_overlap_edges(data, k=3):
    print(u, v)
