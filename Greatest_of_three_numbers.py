first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

largest_number = first_number

if second_number > largest_number:
    largest_number = second_number
if third_number > largest_number:
    largest_number = third_number

print("Largest number is:", largest_number)
