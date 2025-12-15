taxable_income = float(input("Enter taxable income: "))

tax_amount = 0

if taxable_income <= 700000:
    tax_amount = 0
else:
    remaining_income = taxable_income

    if remaining_income > 1500000:
        tax_amount += (remaining_income - 1500000) * 0.30
        remaining_income = 1500000
    if remaining_income > 1200000:
        tax_amount += (remaining_income - 1200000) * 0.20
        remaining_income = 1200000
    if remaining_income > 900000:
        tax_amount += (remaining_income - 900000) * 0.15
        remaining_income = 900000
    if remaining_income > 600000:
        tax_amount += (remaining_income - 600000) * 0.10
        remaining_income = 600000
    if remaining_income > 300000:
        tax_amount += (remaining_income - 300000) * 0.05

cess = tax_amount * 0.04
total_tax_payable = tax_amount + cess

print("Basic Tax:", tax_amount)
print("Cess (4%):", cess)
print("Total Tax Payable:", total_tax_payable)
