# check if elelments in a list are unique if dublicate is found exit the loop and print the dublicate

items=["apple","banana","mango","orange","apple"]
unique_items=set()
for i in items:
    if i in unique_items:
        print("dublicate",i)
        break
    unique_items.add(i)
    


    

