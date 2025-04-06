data = \
    """
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
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
    """

# 讀入資料，將sequence存入dict
sequences = dict()
label = ""
for line in data.splitlines():
    line = line.strip()  # 縮排防呆
    if line:
        if line[0] == ">":
            label = line[1:].strip()  # 去除label頭尾空白
            sequences[label] = ""
        else:
            if label:
                sequences[label] += line

# 針對每一個序列進行GC計算
max_gc_label, max_gc_ratio = "", 0
for label, seq in sequences.items():
    count_a, count_c, count_g, count_t = seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")

    gc_count = count_g + count_c
    total = count_a + count_c + count_g + count_t

    if total == 0:
        gc_ratio = 0  # skip，避免除以0
    else:
        gc_ratio = gc_count / total * 100
    if gc_ratio > max_gc_ratio:
        max_gc_label, max_gc_ratio = label, gc_ratio

print(max_gc_label)
print(f"{max_gc_ratio:.6f}")
