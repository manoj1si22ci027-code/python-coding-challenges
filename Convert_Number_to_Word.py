number = str(input("Enter number: "))

digit_words = ["Zero", "One", "Two", "Three", "Four",
               "Five", "Six", "Seven", "Eight", "Nine"]

for digit in number:
    print(digit_words[int(digit)], end=" ")
