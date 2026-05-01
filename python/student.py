# READ DATA
def read_data():
    file = open("student.txt", "r")
    lines = file.readlines()

    data = {}   # initialize dictionary

    for line in lines:
        line = line.replace("\n", "").split(", ")
        data[line[0]] = [line[1], int(line[2])]

    file.close()
    return data


# ADD STUDENT
def add_student(data):
    sid = input("Enter ID: ")
    
    if sid in data:
        print("ID already exists")
        return

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    data[sid] = [name, marks]
    print("Student added")


# UPDATE MARKS
def update_marks(data):
    sid = input("Enter ID: ")

    if sid not in data:
        print("Invalid ID")
        return

    marks = int(input("Enter new marks: "))

    if marks < 0 or marks > 100:
        print("Marks must be 0-100")
        return

    data[sid][1] = marks
    print("Marks updated")


# SAVE DATA
def save_data(data):
    file = open("student.txt", "w")

    for sid in data:
        file.write(sid + ", " + data[sid][0] + ", " + str(data[sid][1]) + "\n")

    file.close()


#MAIN
data = read_data()

add_student(data)
update_marks(data)

save_data(data)

print("\nFinal Data:")
for sid in data:
    print(sid, data[sid][0], data[sid][1])
                         
