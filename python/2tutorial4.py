N=int(input("Enter N: "))
List =[]

for i in range (N):
    num= int(input("Enter  a number"))
    List.append(num)
print(List)

#[5,2,7,4,1]

max=List[0]
min=List[0]
for each in List:
     if each >max:
        max=each
     if each<min:
        min=each
print(max)
print(min)

    

    
