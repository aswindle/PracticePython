name = input("Enter your name: ")
age = int(input("Enter your age: "))
copies = int(input("How many message copies?"))
year = 2117 - age
print(copies * ("Hello, " + name + ". You will be 100 in the year " + str(year)+".\n"))