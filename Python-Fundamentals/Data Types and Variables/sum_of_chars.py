number_of_characters = int(input())
sum_of_ascii_codes = 0
for i in range(number_of_characters):
    character = input()
    sum_of_ascii_codes += ord(character)
print(f"The sum equals: {sum_of_ascii_codes}")
