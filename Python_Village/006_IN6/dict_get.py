s = "We tried list and we tried dicts also we tried Zen"

counts = dict()
for word in s.split():
    counts[word] = counts.get(word, 0) + 1

for key,value in counts.items():
    print(key, value)