student = input()
while student != "Welcome!":
    house = ""
    if len(student) < 5:
        house = "Gryffindor"
    elif len(student) == 5:
        house = "Slytherin"
    elif len(student) == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"
    if student == "Voldemort":
        print("You must not speak of that name!")
        break
    print(f"{student} goes to {house}.")
    student = input()
else:
    print("Welcome to Hogwarts.")
