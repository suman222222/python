def read_sales_data(sales):
    data=[]
    file=open(sales,"r")
    lines=file.readlines()#reads   all data
    for line in lines:
        line=line.replace('/n','').split(",")#convert string to list
        #print(line)
        data.append([line[1], line[2], line[3]])
    file.close()
    return data
processed_data=read_sales_data("sales.txt")
print (processed_data)


#list of lists
top_product={"name":"","revenue":0}
for each in processed_data:
    print(each)
    name=each[0]
    unit=int(each[1])
    price=float(each[2])
    revenue=unit * price

    if revenue > top_product["revenue"]:
        top_product["name"]=name
        top_product["revenue"]=revenue

print(top_product)

#sale_report

def write_sales_report(output_path, processed_data, top_product):
    file = open(output_path, "w")
    file.write("Product Sales Report\n")
    file.write("--------------------\n")
    for each in processed_data:
        name    = each[0]
        unit    = int(each[1])
        price   = float(each[2])
        revenue = unit * price
        file.write(f"Product: {name}\n")
        file.write(f"Units Sold: {unit}\n")
        file.write(f"Price per Unit: Rs. {price}\n")
        file.write(f"Total Revenue: Rs. {revenue}\n")
        file.write("--------------------\n")
    file.write(f"\nTop Revenue Product\n")
    file.write(f"The top product is {top_product['name']}, generating Rs. {top_product['revenue']} in revenue.\n")
    file.close()

write_sales_report("sales.txt", processed_data, top_product)
print("Report written!")








        
