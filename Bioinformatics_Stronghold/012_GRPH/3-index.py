from collections import defaultdict
from typing import Tuple, Iterator

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


def find_overlap_edges(data: str, k: int = 3) -> Iterator[Tuple[str, str]]:
    seqs = parse_fasta(data)
    prefix = defaultdict(list) # 建立prefix index
    for label, seq in seqs.items():
        if len(seq) >= k:
            prefix[seq[:k]].append(label)


    for src, seq in seqs.items():
        suffix = seq[-k:]
        for dst in prefix.get(suffix, ()):
            if dst != src:  # 剔除掉自我配對（self-loop）
                yield src, dst
    ## 上面 yield 寫法，等價以下寫法
    # edges: list[tuple[str, str]] = []
    # for src, seq in seqs.items():
    #     suffix = seq[-k:]
    #     for dst in prefix.get(suffix, ()):
    #         if src != dst:  # 剔除掉自我配對（self-loop）
    #             edges.append((src, dst))
    # return edges

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

edges = sorted(find_overlap_edges(data, 3))
for u, v in edges:
    print(u, v)
