def process_2d_list(num_list):
    # Initialize max and min values with the first element of the list
    max_num = num_list[0][0]
    min_num = num_list[0][0]

    for row in num_list:
        for num in row:
            print(num)  # Print each number
            if num % 2 == 0 and num % 3 == 0:
                print(f"{num} is divisible by both 2 and 3")
            # Update max_num and min_num
            max_num = max(max_num, num)
            min_num = min(min_num, num)

    print("Max num:", max_num)
    print("Min num:", min_num)

# Test the function
a = [[24, 3, 6],
     [8, 12, 18],
     [2, 66, 7]]
process_2d_list(a)
