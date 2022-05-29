divisor = int(input())
boundary = int(input())
max_number = 0
for num in range(1, boundary + 1):
    if num % divisor == 0:
        max_number = num
print(max_number)
