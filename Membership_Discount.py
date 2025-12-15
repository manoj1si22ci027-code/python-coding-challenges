grand_total = float(input("Enter amount after discounts: "))
membership_status = input("Are you a member (y/n): ")

if membership_status.lower() == 'y':
    grand_total -= grand_total * 0.02

print("Final amount after membership discount:", grand_total)
