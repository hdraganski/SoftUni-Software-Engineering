string = input()
lst = []
for char in range(len(string)):
    if string[char].isupper():
        lst.append(char)
print(lst)
