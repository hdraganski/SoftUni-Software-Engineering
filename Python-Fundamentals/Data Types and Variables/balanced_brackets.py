number_of_lines = int(input())
new_string = ''
for i in range(1, number_of_lines + 1):
    string = input()
    if string == "(":
        new_string += string
    elif string == ")":
        new_string += string
if len(new_string) % 2 == 0 and not("((" in new_string or "))" in new_string):
    print("BALANCED")
else:
    print("UNBALANCED")
