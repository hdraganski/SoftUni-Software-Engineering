string = input()
check = ["sand", "water", "fish", "sun"]
counter = 0
for i in range(len(check)):
    counter += string.lower().count(check[i])
print(counter)