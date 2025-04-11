import itertools

items = ['A', 'B', 'C']
# items = ['A', 'A', 'B', 'B', 'C', 'C']

combs = list(itertools.combinations(items, 2))

print(combs)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(len(combs))  # 3
