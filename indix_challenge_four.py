#SELECT UNIQ(store) FROM products WHERE in_stock=false

#UNIQ(store)
#1
#2
#5
#6
#7

newlist=[]
with open('sql_engine_dataset.csv') as fileop:
    for line in (fileop.readlines()):
        list_new=line.strip().split(",")
        

        if(list_new[4]=='false'):
         newlist.append(list_new[2])

# Duplicate values are removed using set and is converted to string
    list_nodupli=set(newlist)
    for li_dupli in list_nodupli:
        print(str(li_dupli))
    
                   
          
                          
          
    
