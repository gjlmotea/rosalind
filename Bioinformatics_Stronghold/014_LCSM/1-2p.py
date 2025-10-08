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
for i in range(len(s_seq)):
    for j in range(i+1, len(s_seq)+1):
        template = s_seq[i:j]
        is_common = True

        for seq in seqs.values():
            if template in seq:
                continue
            else:
                is_common = False
        if is_common:
            if len(best) < len(template):
                best = template
        # 以上比對，也可簡化成all()寫法：
        # if all(template in seq for seq in seqs.values()):
        #     if len(template) > len(best):
        #         best = template

print(best)