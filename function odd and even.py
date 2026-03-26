# Question 1 - Divisible by 2 and 3

def divisible_by_2_and_3():
    a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]

    for num in a:
        if num % 2 == 0 and num % 3 == 0:
            print(num)


# Question 1 - Divisible by 4 and 5

def divisible_by_4_and_5():
    a = [10, 20, 25, 30, 40, 45, 50, 60, 80, 85, 100]

    for num in a:
        if num % 4 == 0 and num % 5 == 0:
            print(num)


# Call functions
divisible_by_2_and_3()
divisible_by_4_and_5()
