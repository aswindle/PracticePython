def print_ans():
    result = ""
    for i in range(length):
        result+=correct[i] + " "
    print(result)

def check_win():
    for i in range(length):
        if word_list[i]!=correct[i]:
            return False
    return True

def add_letter(guess):
    for i in range(length):
        if word_list[i] == guess:
            correct[i] = guess

word = "EVAPORATE"
length = len(word)
word_list = []
for i in range(length):
    word_list.append(word[i])
correct = []
for i in range(length):
    correct.append("_")
guesses = []
print_ans()
while not check_win():
    guess = input("Guess a letter: ").upper()
    while guess in guesses:
        guess = input("Tried that already. Guess a letter: ").upper()
    guesses.append(guess)
    add_letter(guess)
    print_ans()
    check_win()
print("Congratulations!")
    