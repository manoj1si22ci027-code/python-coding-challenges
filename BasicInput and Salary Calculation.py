employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

basic_monthly_salary = float(input("Enter basic monthly salary: "))
special_allowance = float(input("Enter special allowance (monthly): "))
bonus_percentage = float(input("Enter bonus percentage: "))

gross_monthly_salary = basic_monthly_salary + special_allowance
annual_bonus = (gross_monthly_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

print("Name:", employee_name)
print("EmpID:", employee_id)
print("Gross Monthly Salary:", gross_monthly_salary)
print("Annual Gross Salary:", annual_gross_salary)
