number = int(input())
capacity_taken = 0
for i in range(number):
    liters_of_water = int(input())
    capacity_taken += liters_of_water
    if capacity_taken > 255:
        capacity_taken -= liters_of_water
        print("Insufficient capacity!")
        continue
print(capacity_taken)
