data = \
    """
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    """

lines = data.splitlines()
lines = [line.strip() for line in lines if line.strip()]

count = 0
for i in range(len(lines[0])):
    if lines[0][i] != lines[-1][i]:
        count += 1

print(count)
