s = "GATGGAACTTGACTACGTAAATT"

for base in s:
    match base:
        case 'T':
            print('U', end='')
        case _:
            print(base, end='')

# for base in s:
#    print('U' if base == 'T' else base, end='')