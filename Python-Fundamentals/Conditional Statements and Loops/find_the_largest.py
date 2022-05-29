number = input()
lst = []
for num in range(len(number)):
    lst.append(int(number[num]))
    lst.sort(reverse=True)
for i in range(len(lst)):
    print(lst[i], end="")