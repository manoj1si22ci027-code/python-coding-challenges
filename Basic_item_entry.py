item_code = input("Enter item code: ")
item_description = input("Enter item description: ")
item_quantity = int(input("Enter quantity: "))
item_price = float(input("Enter price per item: "))

item_total = item_quantity * item_price

print("Item Code:", item_code)
print("Item Description:", item_description)
print("Item Total Cost:", item_total)
