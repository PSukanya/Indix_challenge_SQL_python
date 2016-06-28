#SELECT* FROM products WHERE store=2
#title,brand,store,price,in_stock
#Apple iPhone 5,2,2,599.99,true
#Nokia Lumia 800,3,2,300,false
#Samsung LED TV 51 inches,4,2,900,true

from __future__ import print_function
import re

i=0
mylist=[]

# with is used so that a file will be closed without performing an explicit operation
with open('sql_engine_dataset.csv') as fileop:
    for line in fileop.readlines():
        list_new=line.strip().split(",") # strip is to remove \n characters when split function is used

# Creating and appending an empty list to retrieve the column values (generic)
# Database can change the column names anytime and this code will not demand a change.
        while(i<len(list_new)):
         mylist.append(list_new[i])
         print(mylist[i],end=' ')
         i=i+1

        if(list_new[2]=='2' ):
            print(" ".join(list_new))
         
    

         

    

    
    
    

       
