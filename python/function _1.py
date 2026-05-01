#write a function that takes a number N as parameters and returns the sum of all the odd numbers from 1 to N

def sum_of_odds(N):
    total=0
    for i in range(1,N+1):
        if i %2!=0:
            total += i
    return total

print(sum_of_odds(10))  # 25
print(sum_of_odds(7))   # 16
print(sum_of_odds(1))   # 1
    
    
