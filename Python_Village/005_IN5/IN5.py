with open("IN5.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):  # 索引從1（第一行）開始，以符合直覺
        if i % 2 == 0:
            print(line.strip())