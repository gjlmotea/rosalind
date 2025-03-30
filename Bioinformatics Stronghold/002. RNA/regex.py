import re

s = "GATGGAACTTGACTACGTAAATT"
rna = re.sub('T', 'U', s) # 替換(substitute)
print(rna)
