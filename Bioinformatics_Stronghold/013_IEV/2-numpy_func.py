import numpy as np

def expected_offspring(raw_data: str, offspring: int = 2) -> float:
    counts = np.fromstring(raw_data, sep=' ', dtype=int)
    weights = np.array([1, 1, 1, 0.75, 0.5, 0], dtype=float)

    if counts.size != weights.size:
        raise ValueError(f"資料長度不符: counts={counts.size}, weights={weights.size}")
    if (counts < 0).any():
        raise ValueError("輸入的配對數不可為負數")

    return float(offspring * counts.dot(weights))

print(expected_offspring("1 0 0 1 0 1"))
