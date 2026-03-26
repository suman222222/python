a=[[24,3,6],
   [8,12,18],
   [2,66,7]]

max_num=a[0][0]
min_num=a[0][0]

for i in range(len(a)):#i=o
    for j in range (len(a[i])):#j=0
        num=a[i][j]#a[0][0]
        print(a[i][j])#a[0][0]
        if num %  2 == 0 and num %3 == 0:
            print(num)
        if num > max_num:
            max_num=num
        if num< min_num:
            min_num= num
print("max num:" ,max_num)
print("min num:" ,min_num)

            
