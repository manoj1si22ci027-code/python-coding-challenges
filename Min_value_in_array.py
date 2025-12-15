number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for _ in range(number_of_elements):
    elements_array.append(int(input("Enter element: ")))

minimum_value = elements_array[0]

for value in elements_array:
    if value < minimum_value:
        minimum_value = value

print("Minimum Value:", minimum_value)
