item_code = input("Enter item code: ")
item_total = float(input("Enter item total: "))

if item_code == "PROMO10":
    item_total -= item_total * 0.10

print("Final Item Total:", item_total)
