grand_total = float(input("Enter grand total: "))
total_quantity = int(input("Enter total quantity: "))

if grand_total > 10000:
    grand_total -= grand_total * 0.10

if total_quantity > 20:
    grand_total -= grand_total * 0.05

print("Total after discounts:", grand_total)
