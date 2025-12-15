employee_name = input("Enter employee name: ")
while not employee_name.isalpha() or len(employee_name) > 50:
    print("Invalid name")
    employee_name = input("Enter employee name: ")

employee_id = input("Enter employee ID: ")
while not employee_id.isalnum() or not (5 <= len(employee_id) <= 10):
    print("Invalid EmpID")
    employee_id = input("Enter employee ID: ")

basic_salary = float(input("Enter basic salary: "))
while basic_salary <= 0 or basic_salary > 10000000:
    print("Invalid basic salary")
    basic_salary = float(input("Enter basic salary: "))

special_allowance = float(input("Enter special allowance: "))
while special_allowance < 0 or special_allowance > 10000000:
    print("Invalid special allowance")
    special_allowance = float(input("Enter special allowance: "))

bonus_percentage = float(input("Enter bonus percentage: "))
while bonus_percentage < 0 or bonus_percentage > 100:
    print("Invalid bonus percentage")
    bonus_percentage = float(input("Enter bonus percentage: "))

print("All inputs are valid")
