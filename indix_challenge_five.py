#SELECT title FROM products WHERE in_stock=false AND brand=5

#title
#L'Oreal Hair Conditioner
#L'Oreal Hair Conditioner

with open('sql_engine_dataset.csv') as fileop:
    for line in fileop.readlines():
        list_new=line.strip().split(",")
        #print(list_new)
        
        if(list_new[1]=='5' and list_new[4]=='FALSE' or list_new[0]=='title'):
            print(list_new[0])
          
