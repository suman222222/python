N = int(input("Enter number of students: "))
M = int(input("Enter number of subjects: "))

students_data = []   # list to store data

# Input data for each student
for i in range(N):
    name = input(f"\nEnter the name of student {i+1}: ")
    marks = []

    for j in range(M):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    students_data.append([name, marks])

# Process and display results
print("\nStudent Report:")

for student in students_data:
    name = student[0]
    marks = student[1]

    # Initialize highest, lowest, total
    highest = marks[0]
    lowest = marks[0]
    total = 0

    # Loop to calculate manually
    for mark in marks:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
        total += mark

    average = total / M

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Non Graded"

    # Print student report
    print(f"\nName: {name}")
    print(f"Marks: {marks}")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
