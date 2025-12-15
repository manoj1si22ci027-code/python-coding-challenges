number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for index in range(number_of_elements):
    value = int(input("Enter element: "))
    elements_array.append(value)

print("Array Elements:", elements_array)
