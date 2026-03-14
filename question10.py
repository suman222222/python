#program to generate a receipt for three items with 13% tax

#input for three items

name1=input("enter name of item 1: ")
price1=float(input("enter the price of item1:"))

name2=input("enter name of item 2: ")
price2=float(input("enter the price of item2:"))

name3=input("enter name of item 3: ")
price3=float(input("enter the price of item3:"))

subtotal= price1 + price2 + price3

#calculating tax

tax= subtotal * 0.13

#Final total
final_total = subtotal+ tax

#Display

print("item 1 Name and Price : " , name1, ",Rs.",price1)
print("item 2 Name and Price : " , name2 , ",Rs.",price2)
print("item 3 Name and Price : " , name3 , ",Rs.",price3)

print("Total cost is : " ,subtotal)
print("tax Amount is : ", tax)
print("final_total is : ", final_total)

