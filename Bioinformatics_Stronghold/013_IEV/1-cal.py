data = "1 0 0 1 0 1"
counts = [int(x) for x in data.split(" ") if x.isdigit()]
weight = [1, 1, 1, 3 / 4, 1 / 2, 0]
offspring = 2

result = [d * w for d, w in zip(counts, weight)]
print(sum(result)*offspring)
