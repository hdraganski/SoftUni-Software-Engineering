number = int(input())
for first_char in range(97, 97 + number):
    for second_char in range(97, 97 + number):
        for third_char in range(97, 97 + number):
            combination = chr(first_char) + chr(second_char) + chr(third_char)
            print(combination)
