s = "GATGGAACTTGACTACGTAAATT"

trans_table = str.maketrans('T', 'U')
rna = s.translate(trans_table)

print(rna)

