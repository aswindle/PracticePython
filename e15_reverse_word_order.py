def reverse(str):
    words = str.split()
    new = []
    for i in range(1, len(words)+1):
        new.append(words[-i])
    return " ".join(new)

text = "Hello this is a long string of text"
print(reverse(text))