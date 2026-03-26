#fibonacci sequence using lists

#output:1,1,2,3,5,8,13,21,34,55

n=int(input("Enter how many Fibonacci numbers to generate:"))
fib=[]
#first two  numbers
if n>=1:
    fib.append(1)
    if n>=2:
        fib.append(1)
        for i in range(2,n):
            next_num=fib[i-1]+fib[i-2]
            fib.append(next_num)
            print("Fibonacci sequence:",fib)
