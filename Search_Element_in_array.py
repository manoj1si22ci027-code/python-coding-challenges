number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for _ in range(number_of_elements):
    elements_array.append(int(input("Enter element: ")))

search_element = int(input("Enter element to search: "))

found = False

for value in elements_array:
    if value == search_element:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")
