#SELECT title FROM products WHERE in_stock=false AND ( brand=5 OR store=2 )

#title
#Nokia Lumia 800
#L'Oreal Hair Conditioner
#L'Oreal Hair Conditioner

with open('sql_engine_dataset.csv') as fileop:
    for line in fileop.readlines():
        line_strip=line.strip()
        list=line_strip.split(",")
        if(list[4]=='false' and (list[1]=='5' or list[2]=='2') or list[0]=='title'):
            print(list[0])


