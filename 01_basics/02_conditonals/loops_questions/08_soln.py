# # check the prime number
# # num=int(input("enter your number"))
# if num>1:
#     for i in range (2,num):
#         if (num%i==0):
#             print("not a prime number")
#             break
#     else:
#         # print("prime no")        
            

# alter natve way by boolean
num=int(input("enter your number"))
is_prime=True
if num>1:
    for i in range(2,num):
        if (num%i==0):
            is_prime=False
    
    
    else:
        print(is_prime) 

      
    