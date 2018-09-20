check = int(input("Enter a max value you want: "))
a = [1,1,2,3,4,8,13,21,34,55,89]
b = []
for i in a:
    if i<check:
        b.append(i)
print(b)  