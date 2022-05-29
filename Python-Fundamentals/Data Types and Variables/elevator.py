persons = int(input())
capacity = int(input())
courses = 0
courses += persons // capacity
if persons % capacity != 0:
    courses += 1
print(courses)
