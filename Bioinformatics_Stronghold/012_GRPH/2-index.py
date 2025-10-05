from collections import defaultdict
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
    heads = defaultdict(list)  # k-前綴
    tails = defaultdict(list)  # k-後綴

    for lbl, s in seqs.items():
        if len(s) >= k: # 檢查長度是否合理（序列長度是否>k值）
            heads[s[:k]].append(lbl)
            tails[s[-k:]].append(lbl)

    edges = []
    # 遍歷同時出現在頭部與尾部的key
    for key in heads.keys() & tails.keys(): # 使用 and operator
        for u in tails[key]:      # suffix
            for v in heads[key]:  # prefix
                if u != v:
                    edges.append((u, v))
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

edges = find_overlap_edges(data, k=3)
for u, v in edges:
    print(u, v)
