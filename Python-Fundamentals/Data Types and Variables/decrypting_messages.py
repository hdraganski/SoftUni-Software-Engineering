key = int(input())
number_of_chars = int(input())
message = ''
for chars in range(number_of_chars):
    char = input()
    message += chr(ord(char) + key)
print(message)
