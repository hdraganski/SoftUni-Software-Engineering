command = input()
events = ["coding", "dog", "cat", "movie"]
count_coffees = 0
while command != "END":
    if command.lower() in events:
        if command.islower():
            count_coffees += 1
        else:
            count_coffees += 2
    if count_coffees > 5:
        print("You need extra sleep")
        break
    command = input()
else:
    print(f"{count_coffees}")
