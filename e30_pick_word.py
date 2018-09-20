import random

with open('sowpods.txt', 'r') as file:
    lines = []
    next = file.readline().strip()
    while next:
        lines.append(next)
        next = file.readline().strip()

word_num = random.randint(0, len(lines))
word = lines[word_num]
print(word)