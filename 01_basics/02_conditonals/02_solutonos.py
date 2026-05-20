# movie ticket price
# movie ticket price based on age :12$ for adukts(18-over),$8 for children,everyone gets $2 discoutn on wednesday
age=int(input("enter your age"))
day=(input("enter name of day"))
if age>18:
    ticket_price=12
else:
    
    ticket_price=8
if day.lower()=="wednesday":
    discount=ticket_price-2
    print("ticket_price is $",discount) 
else:
    print(ticket_price)    
       
    
    
         

    