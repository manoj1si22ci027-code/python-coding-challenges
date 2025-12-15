number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for _ in range(number_of_elements):
    elements_array.append(int(input("Enter element: ")))

elements_array.sort()

print("Sorted Array:", elements_array)

search_element = int(input("Enter element to search: "))

low_index = 0
high_index = number_of_elements - 1
found = False

while low_index <= high_index:
    middle_index = (low_index + high_index) // 2

    if elements_array[middle_index] == search_element:
        found = True
        break
    elif elements_array[middle_index] < search_element:
        low_index = middle_index + 1
    else:
        high_index = middle_index - 1

if found:
    print("Element Found")
else:
    print("Element Not Found")
