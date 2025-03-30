def reverse_complement(dna):
    table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = str()
    for base in reversed(dna):
        result += table[base]
    return result

s = "AAAACCCGGT"
print(reverse_complement(s))
