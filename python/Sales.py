def read_sales_data(file_path):
    sales_data = {}

    try:
        file = open(file_path, "r")
        lines = file.readlines()

        for line in lines:
            line = line.strip().split(",")

            item_id = int(line[0])
            name = line[1]
            quantity = int(line[2])
            price = float(line[3])

            sales_data[item_id] = [name, quantity, price]

        file.close()

    except FileNotFoundError:
        print("Error: File not found!")

    return sales_data

def display_sales_data(sales_data):
    print("\n--- SALES DATA ---")
    print("ID\tName\t\tQuantity\tPrice")

    for key, value in sales_data.items():
        if len(value[0]) < 8:
            print(f"{key}\t{value[0]}\t\t{value[1]}\t\t{value[2]}")
        else:
            print(f"{key}\t{value[0]}\t{value[1]}\t\t{value[2]}")

def update_quantity(sales_data):
    try:
        item_id = int(input("\nEnter Item ID to update quantity: "))

        if item_id in sales_data:
            quantity = int(input("Enter quantity to add: "))

            if quantity > 0:
                sales_data[item_id][1] += quantity
                print("Quantity updated successfully!")
            else:
                print("Invalid quantity!")
        else:
            print("Item ID not found!")

    except ValueError:
        print("Invalid input!")

def update_item_price(sales_data):
    try:
        item_id = int(input("\nEnter Item ID to update price: "))

        if item_id in sales_data:
            price = float(input("Enter new price: "))

            if price > 0:
                sales_data[item_id][2] = price
                print("Price updated successfully!")
            else:
                print("Invalid price!")
        else:
            print("Item ID not found!")

    except ValueError:
        print("Invalid input!")

def write_sales_data(file_path, sales_data):
    file = open(file_path, "w")

    for key, value in sales_data.items():
        file.write(f"{key},{value[0]},{value[1]},{value[2]}\n")

    file.close()
    print("File updated successfully!")

def write_report(file_name, sales_data):
    file = open(file_name, "w")

    file.write("PRODUCT SALES REPORT\n")
    file.write("====================\n\n")

    total = 0

    for key, value in sales_data.items():
        revenue = value[1] * value[2]
        total += revenue

        file.write(f"ID: {key}\n")
        file.write(f"Product: {value[0]}\n")
        file.write(f"Quantity: {value[1]}\n")
        file.write(f"Price: {value[2]}\n")
        file.write(f"Revenue: {revenue}\n")
        file.write("----------------------\n")

    file.write(f"\nTotal Revenue: {total}")

    file.close()
    print("Report created successfully!")

def main():
    file_path = "sales.txt"

    sales_data = read_sales_data(file_path)

    display_sales_data(sales_data)

    update_quantity(sales_data)
    update_item_price(sales_data)

    display_sales_data(sales_data)

    write_sales_data(file_path, sales_data)
    write_report("sales_report.txt", sales_data)

main()
