def dominant_probability(k, m, n):
	total = k + m + n

	prob = 0
	prob += (k / total) * ((k - 1) / (total - 1)) * 1  # AA x AA
	prob += (k / total) * (m / (total - 1)) * 1  # AA x Aa
	prob += (m / total) * (k / (total - 1)) * 1  # Aa x AA
	prob += (k / total) * (n / (total - 1)) * 1  # AA x aa
	prob += (n / total) * (k / (total - 1)) * 1  # aa x AA
	prob += (m / total) * ((m - 1) / (total - 1)) * 0.75  # Aa x Aa
	prob += (m / total) * (n / (total - 1)) * 0.5  # Aa x aa
	prob += (n / total) * (m / (total - 1)) * 0.5  # aa x Aa
	prob += (n / total) * ((n - 1) / (total - 1)) * 0  # aa x aa

	return prob


print(dominant_probability(2, 2, 2))
