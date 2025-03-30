s = "GATGGAACTTGACTACGTAAATT"

# print(s.replace('T', 'U'))

def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')

print(transcribe_dna_to_rna(s))
