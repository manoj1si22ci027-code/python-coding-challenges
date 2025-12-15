number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for _ in range(number_of_elements):
    elements_array.append(int(input("Enter element: ")))

sort_order = input("Enter sort order (asc/desc): ")

if sort_order == "asc":
    elements_array.sort()
elif sort_order == "desc":
    elements_array.sort(reverse=True)

print("Sorted Array:", elements_array)
