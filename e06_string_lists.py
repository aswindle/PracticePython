word = input("Enter a word: ")
palindrome = True
for x in range(0, len(word)//2):
    if word[x] != word[-(x+1)]:
        palindrome = False
        break
print(palindrome)