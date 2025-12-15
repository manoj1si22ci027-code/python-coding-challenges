student_name = input("Enter student name: ")

subject1_marks = float(input("Enter marks for subject 1: "))
subject2_marks = float(input("Enter marks for subject 2: "))
subject3_marks = float(input("Enter marks for subject 3: "))

total_marks = subject1_marks + subject2_marks + subject3_marks
average_marks = total_marks / 3

if average_marks >= 60:
    result_class = "1st Class"
elif average_marks >= 50:
    result_class = "2nd Class"
elif average_marks >= 35:
    result_class = "Pass Class"
else:
    result_class = "Fail"

print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Class Secured:", result_class)
