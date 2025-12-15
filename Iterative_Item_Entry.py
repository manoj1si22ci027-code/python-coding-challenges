number_of_items = int(input("Enter number of items: "))

grand_total = 0

for _ in range(number_of_items):
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    grand_total += quantity * price

print("Grand Total:", grand_total)
