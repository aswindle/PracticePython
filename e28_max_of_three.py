def max_three(a, b, c):
    biggest = a
    if b > biggest: biggest = b
    if c > biggest: biggest = c
    return biggest

print(max_three(6,2,4)) 