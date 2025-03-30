from collections import defaultdict

def count_word_occurrences(s):
    counts = defaultdict(int)  # 使用defaultdict來將value初始化為0

    for word in s.split():
        counts[word] += 1

    for word, count in counts.items():
        print(word, count)


s = "We tried list and we tried dicts also we tried Zen"
count_word_occurrences(s)