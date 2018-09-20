def count_cows(guess): #if items in same position are correct it counts as a cow
    cows = 0
    guess_digits = [0,0,0,0]
    new = guess
    for i in range(1, 5):
        guess_digits[-i] = new%10
        new = new//10
    for i in range(0, 4):
        if guess_digits[i]==digits[i]:
            cows+=1
    return cows

def count_bulls(guess): #if item is in the list but not at that spot it counts as a bull
    bulls = 0
    guess_digits = [0,0,0,0]
    new = guess
    for i in range(1, 5):
        guess_digits[-i] = new%10
        new = new//10
    for i in range(0, 4):
        if guess_digits[i] in digits and guess_digits[i] != digits[i]:
            bulls += 1
    return bulls

import random
correct = random.randint(1000, 9999)
print("Correct: " + str(correct))
digits = [0,0,0,0]
new = correct
for i in range(1, 5):
    digits[-i] = new%10
    new = new//10
guess = int(input("Guess a 4-digit number: "))
tries = 1
while(guess!=correct):
    print("Your guess: " + str(guess))
    print("Cows: " + str(count_cows(guess)))
    print("Bulls: " + str(count_bulls(guess)))
    tries+=1
    guess = int(input("Guess a 4-digit number: "))
print("Correct! It took you " + str(tries) + " tries.")
    