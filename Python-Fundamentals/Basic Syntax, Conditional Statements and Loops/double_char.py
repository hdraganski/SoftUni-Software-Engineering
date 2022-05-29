string = input()
while string != "End":
    new_string = ""
    if string != "SoftUni":
        for index, char in enumerate(string):
            new_string += char * 2
        print(new_string)
    string = input()
