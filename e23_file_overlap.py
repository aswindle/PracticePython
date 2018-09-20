with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline().strip()
    happy = []
    while line:
        num = int(line)
        if num not in happy:
            happy.append(num)
        line = open_file.readline().strip()

with open('primenumbers.txt', 'r') as open_file2:
    line = open_file2.readline().strip()
    prime = []
    while line:
        num = int(line)
        if num not in prime:
            prime.append(num)
        line = open_file2.readline().strip()

both = []
for x in range(0, len(happy)):
    if happy[x] in prime:
        both.append(happy[x])
print(both)