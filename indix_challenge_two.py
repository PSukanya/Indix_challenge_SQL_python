#SELECT brand FROM products WHERE price > 600
#brand
#2
#2
#4
#4
#4

# Opening a file using with keyword as it closes automatically
with open('sql_engine_dataset.csv') as fileop:
    for line in fileop.readlines():
        list=line.strip().split(",")

# Comparing the prices less than 600 to fetch the brand values
        if(list[3] >'600.00'):
            print(list[1])


