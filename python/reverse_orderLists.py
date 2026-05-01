#original list
l=[1,2,3,4,5,6,7,8,9]
#creates empty list
reverse_list=[]
for i in range (len(l)-1,-1,-1):#loop from last element to first
    reverse_list.append(l[i])
    print("Original List:",l)
    print("Reversed List:",reverse_list)
    

    
    
