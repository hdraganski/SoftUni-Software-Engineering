number_of_strings = int(input())
for num in range(number_of_strings):
    string = input()
    if string.find("_") != -1 or string.find(",") != -1 or string.find(".") != -1:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
