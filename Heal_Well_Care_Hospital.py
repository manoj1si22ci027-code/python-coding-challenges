services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

GST_RATE = 0.18
SENIOR_DISCOUNT_RATE = 0.10
HIGH_BILL_DISCOUNT_RATE = 0.05

patient_name = input("Enter Patient Name: ")
patient_age = int(input("Enter Age: "))
patient_gender = input("Enter Gender: ")
patient_contact = input("Enter Contact Number: ")

print("\nAvailable Services:")
for index, service in enumerate(services, start=1):
    print(f"{index}. {service}")

selected_indices = list(
    map(int, input("\nEnter service numbers (comma separated): ").split(","))
)

selected_services = []
selected_costs = []

for index in selected_indices:
    selected_services.append(services[index - 1])
    selected_costs.append(costs[index - 1])

subtotal = sum(selected_costs)

discount_amount = 0

if patient_age >= 60:
    discount_amount += subtotal * SENIOR_DISCOUNT_RATE

subtotal_after_senior_discount = subtotal - discount_amount

if subtotal_after_senior_discount > 5000:
    discount_amount += subtotal_after_senior_discount * HIGH_BILL_DISCOUNT_RATE

final_subtotal = subtotal - discount_amount

gst_amount = final_subtotal * GST_RATE
grand_total = final_subtotal + gst_amount

print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("\nPatient Information:")
print(f"Name   : {patient_name}")
print(f"Age    : {patient_age}")
print(f"Gender : {patient_gender}")
print(f"Contact: {patient_contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i + 1}. {selected_services[i]}: ₹{selected_costs[i]}")

print(f"\nSubtotal           : ₹{subtotal}")
print(f"Discount Applied   : ₹{discount_amount:.2f}")
print(f"GST (18%)          : ₹{gst_amount:.2f}")
print(f"Grand Total        : ₹{grand_total:.2f}")

print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
