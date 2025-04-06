def hamming_distance(s: str, t: str) -> int:
    total = 0
    zipped = zip(s, t)
    for a, b in zipped:
        if a != b:
            total += 1

    return total
    # return sum(1 for a, b in zip(s, t) if a != b) # 單行精簡寫法

# 手動拆分兩序列
source = "GAGCCTACTAACGGGAT"
target = "CATCGTAATGACGGCCT"
print(hamming_distance(source, target))
