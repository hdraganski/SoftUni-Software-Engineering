budget = int(input())
command = input()
money_is_over = False
while command != "End":
    current_price = int(command)
    budget -= current_price
    if budget < 0:
        money_is_over = True
        break
    command = input()
if not money_is_over:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")
