#SELECT MAX(price) FROM products

#MAX(price)
#1099.99

max_price=0
newlist=[]
with open('sql_engine_dataset.csv') as fileop:
    for line in fileop.readlines():
        list=line.strip().split(",")

# The price values are converted to integer and the maximum value is retrieved from the list using max function     
        if ( list[3] not in 'price' ):
            newlist.append(float(list[3]))
            
print (max(newlist))
        
        
        
