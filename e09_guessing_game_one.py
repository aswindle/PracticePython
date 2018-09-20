import random
num = random.randint(1,9)
tries = 1
guess = int(input("Guess a number from 1 to 9"))
while(guess!=num):
    if(guess>num):
        print("Too high")
    else: print("Too low")
    tries += 1
    guess = int(input("Guess a number from 1 to 9"))
print("Correct! It took you " + str(tries) + " guesses.")