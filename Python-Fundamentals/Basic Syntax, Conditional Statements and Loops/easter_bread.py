budget = float(input())
price_per_kg_flour = float(input())
price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_250ml_milk = price_per_kg_flour * 1.25 / 4
total_price = price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk
count_eggs = 0
count_loaves = 0
while budget > 0:
    if budget - total_price < 0:
        break
    budget -= total_price
    count_eggs += 3
    count_loaves += 1
    if count_loaves % 3 == 0:
        count_eggs -= (count_loaves - 2)
print(f"You made {count_loaves} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
