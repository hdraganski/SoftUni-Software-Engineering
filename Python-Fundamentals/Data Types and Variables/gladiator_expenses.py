lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
count_shield_brakes = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        total_price += helmet_price
    if fight % 3 == 0:
        total_price += sword_price
        if fight % 2 == 0:
            total_price += shield_price
            count_shield_brakes += 1
    if count_shield_brakes == 2:
        total_price += armor_price
        count_shield_brakes = 0
print(f"Gladiator expenses: {total_price:.2f} aureus")
