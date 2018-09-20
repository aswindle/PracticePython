locations = {}
with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        next_slash = line.index('/', 3, len(line))
        location = line[3:next_slash]
        if location not in locations:
            locations[location] = 1
        else:
            locations[location] += 1
        line = open_file.readline()
print(locations)

names = {}
with open('nameslist.txt', 'r') as open_file2:
    line = open_file2.readline().strip()
    while line:
        if line not in names:
            names[line] = 1
        else:
            names[line] += 1
        line = open_file2.readline().strip()
print(names)