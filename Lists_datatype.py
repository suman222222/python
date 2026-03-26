#sum of odd numbers and sum of even numbers

print("Task:sum of odd and even numbers")
count1=int(input("How many numbers do you want to enter?"))
numbers1=[]
for i in range(count1):
      value =int(input("Enter numbers " + str(i+1) +":"))
      numbers1.append(value)
      odd_sum=0
      even_sum=0
      for num in numbers1:
          if num%2==0:
              even_sum=even_sum+num
          else:
              odd_sum=odd_sum+num
              print("List:",numbers1)
              print("Sum of odd numbers:",odd_sum)
              print("Sum of even numbers:",even_sum)
