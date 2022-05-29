n = int(input())
for number in range(1, n + 1):
    is_special = False
    tot = 0
    i = number
    while i > 0:
        tot += i % 10
        i //= 10
    if tot == 5 or tot == 7 or tot == 11:
        is_special = True
    print(f"{number} -> {is_special}")
