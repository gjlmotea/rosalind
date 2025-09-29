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

def parse_fasta(data: str) -> dict:
	sequences = {}
	label = ""
	for line in data.strip().splitlines():
		line = line.strip()  # 縮排防呆
		if not line:  # 跳過空行
			continue
		if line.startswith(">"):
			label = line[1:].strip()  # 去除label頭尾空白
			if not label:  # 跳過空標籤（不合法）
				label = ""
				continue
			sequences[label] = ""
		elif label:
			sequences[label] += line

	return sequences


seqs = parse_fasta(data)
print(seqs)

for s1 in seqs:
	for s2 in seqs:
		if s1 == s2:
			continue
		if seqs[s1][-3:] == seqs[s2][:3]:
			print(s1, s2)
