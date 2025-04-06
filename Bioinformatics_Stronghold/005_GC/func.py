def parse_fasta(data):
    sequences = dict()
    label = ""
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            label = line[1:].strip()
            sequences[label] = ""
        elif label:
            sequences[label] += line

    return sequences

def get_gc_content(seq):
    total = seq.count("A")+seq.count("C")+seq.count("G")+seq.count("T")
    if total == 0:
        return 0
    gc_content = (seq.count("G")+seq.count("C")) / total * 100

    return gc_content

def find_highest_gc(fasta_str):
    sequences = parse_fasta(fasta_str)
    max_gc_label, max_gc_ratio = "", 0
    for label, sequence in sequences.items():
        gc_content = get_gc_content(sequence)
        if gc_content > max_gc_ratio:
            max_gc_label, max_gc_ratio = label, gc_content

    return max_gc_label, max_gc_ratio

data = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

label, gc_ratio = find_highest_gc(data)
print(label)
print(f"{gc_ratio:.6f}")
