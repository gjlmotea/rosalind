import numpy as np

raw_data = "1 0 0 1 0 1"

# counts = np.fromstring(raw_data, sep=' ', dtype=int) # 指定dtype寫法
counts = np.fromstring(raw_data, sep=' ')

weights = np.array([1, 1, 1, 0.75, 0.5, 0])
# weights = np.array([1, 1, 1, 0.75, 0.5, 0], dtype=float) # 指定dtype寫法

offspring = 2

expected = offspring * counts.dot(weights)  # = 2 * Σ(counts_i * weights_i)

print(expected)
