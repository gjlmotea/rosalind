import itertools

def dominant_probability(k, m, n):
	# 產出所有基因池可能性
	pool = ['AA'] * k + ['Aa'] * m + ['aa'] * n  # ['AA', 'AA', 'Aa', 'Aa', 'aa', 'aa']

	total = 0
	count = 0  # 計算顯性後代(dominant offspring)的數量

	for a, b in itertools.combinations(pool, 2):
		total += 1

		pair = {a, b}  # 用集合去重複、不管先後順序
		# 1. ex: ('AA','AA') 變成 ('AA')
		# 2. ex: ('AA', 'Aa') 等同於 ('Aa', 'AA')

		print(pair)
		if pair == {'AA'}:
			count += 1
		elif pair == {'Aa'}:
			count += 0.75
		elif pair == {'aa'}:
			count += 0
		elif pair == {'AA', 'Aa'}:
			count += 1
		elif pair == {'AA', 'aa'}:
			count += 1
		elif pair == {'Aa', 'aa'}:
			count += 0.5

	return count / total

print(dominant_probability(2, 2, 2))
