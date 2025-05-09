def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return []

    # 建立壞字元表
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    print(bad_char)

    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            result.append(shift + 1)  # 1-based index
            # 原本是 shift += m，但這會跳過重疊
            # 改為根據下一個壞字元跳，或至少右移一格
            shift += 1
        else:
            last = bad_char.get(text[shift + j], -1)
            shift += max(1, j - last)

    return result


s = "GATATATGCATATACTT"
sub = "ATAT"

print(boyer_moore(s, sub))
