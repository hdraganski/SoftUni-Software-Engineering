first_string = input()
second_string = input()
unique_string = first_string
for char in range(len(first_string)):
    current_string = second_string[:char + 1]
    current_string += first_string[char + 1:]
    if current_string != unique_string:
        unique_string = current_string
        print(unique_string)