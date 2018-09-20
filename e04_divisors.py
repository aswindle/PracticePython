num = int(input("Enter a number to check divisors: "))
divisors = [1]
for x in range(2, num):
    if num % x == 0:
        divisors.append(x)
print(divisors)