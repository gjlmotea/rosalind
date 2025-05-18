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

data = \
	"""
>我的序列01
AAAAA
A
A
A
> 我的序列02
CCCC
CCCC

> 我的序列 03
GGGGGGGG

> 神的序列>>>
ATCGATCG

>鬼的序列
>>>

	>不小心縮排
	TTTT

>   
ATGC
（空白標籤不合法，應捨棄這段序列）
	
"""

seqs = parse_fasta(data)
print(seqs)
