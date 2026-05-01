N=int(input ("enter N:"))
student={}

for i in range (N):
    name=input("Enter Name :")
    marks=float(input("Enter marks :"))

    student[name]=marks

print(student)

for key, value in student.items():
    print(key, value)


