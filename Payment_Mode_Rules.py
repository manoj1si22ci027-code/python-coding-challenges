final_amount = float(input("Enter final amount: "))
payment_mode = input("Enter payment mode (Cash/Card): ")

if payment_mode.lower() == "card":
    surcharge = final_amount * 0.02
    final_amount += surcharge
    print("Surcharge Applied:", surcharge)
print(f"Payment methid: {payment_mode}")
print("Payable Amount:", final_amount)
