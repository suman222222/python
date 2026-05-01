#given List
numbers=[1,1,2,3,3,4,4,5,6,5,6,7,7,8,9,9,10]
#create empty list for unique elements/new updateed list

unique_list=[]
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
        print("Original List:",numbers)
        print("Unique List of elements:",unique_list)
