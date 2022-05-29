string = input()
lst = string.split(", ")
lst.reverse()
for i in range(len(lst)):
    if lst[i] == "wolf":
        if i == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")

