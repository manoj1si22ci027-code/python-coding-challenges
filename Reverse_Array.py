number_of_elements = int(input("Enter number of elements: "))

elements_array = []

for _ in range(number_of_elements):
    elements_array.append(int(input("Enter element: ")))

reversed_array = []
#We can use built in Reverse function also
for index in range(number_of_elements - 1, -1, -1):
    reversed_array.append(elements_array[index])

print("Reversed Array:", reversed_array)
