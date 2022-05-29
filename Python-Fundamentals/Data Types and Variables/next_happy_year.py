number = int(input())
is_happy = False
new_number = number
while not is_happy:
    new_number += 1
    if len(set(str(new_number))) == len(str(number)):
        is_happy = True
        print(new_number)
        break

