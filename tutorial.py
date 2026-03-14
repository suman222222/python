n=int(input("Enter n:"))
sum_even =0
sum_odd = 0
for i in range (n):
    num=int(input("enter a number:"))
    list=[]
    list.append(num)
    print(list)
for each in list:
        if each%2==0:
            sum_even += each
        else:
            sum_odd += each
print("Sum of even Numbers:",sum_even)
print("Sum of odd Numbers:",sum_odd)
