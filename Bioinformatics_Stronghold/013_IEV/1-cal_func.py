def expected_offspring(raw_data: str, offspring: int = 2) -> float:
    weight = [1, 1, 1, 0.75, 0.5, 0]
    counts = [int(x) for x in raw_data.split() if x.isdigit()]

    if len(counts) != len(weight):
        raise ValueError(f"資料長度不符: data={len(counts)}, weight={len(weight)}")
    if any(d < 0 for d in counts):
        raise ValueError("輸入的配對數不可為負數")

    return offspring * sum(d * w for d, w in zip(counts, weight))

print(expected_offspring("1 0 0 1 0 1"))
