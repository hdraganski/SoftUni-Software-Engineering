number_of_messages = int(input())
result = ""
for i in range(number_of_messages):
    message = int(input())
    if message == 88:
        result = "Hello"
    elif message == 86:
        result = "How are you?"
    elif message > 88:
        result = "Bye."
    else:
        result = "GREAT!"
    print(f"{result}")
