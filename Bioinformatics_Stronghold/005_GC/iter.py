data = \
""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

# 讀入資料，將sequence存入dict
sequences = dict()
label = ""
for line in data.splitlines():
    if line[0] == ">":
        label = line[1:]
        sequences[label] = ""
    else:
        sequences[label] += line

# 針對每一個序列進行GC計算
max_gc_label, max_gc_ratio = "", 0
for label, seq in sequences.items():
    at_count = 0
    gc_count = 0
    for base in seq:
        if base == 'A' or base == 'T':
            at_count += 1
        if base == 'C' or base == 'G':
            gc_count += 1
    gc_ratio = gc_count / (at_count + gc_count) * 100
    if gc_ratio > max_gc_ratio:
        max_gc_label, max_gc_ratio = label, gc_ratio

print(max_gc_label)
print(f"{max_gc_ratio:.6f}")
