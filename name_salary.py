employee_name = input("Enter employee name: ")
annual_salary = float(input("Enter annual salary: "))

if annual_salary > 300000:
    print(employee_name, "must pay tax")
else:
    print(employee_name, "does not need to pay tax")
