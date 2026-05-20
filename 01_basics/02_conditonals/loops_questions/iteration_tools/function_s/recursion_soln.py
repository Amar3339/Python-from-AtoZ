# create  a recurssi0n fn that calculate the factorial of number:
def factorial(n):
    if n==0:
        return 1
    
    else:
         return n*factorial(n-1)
   
    
print(factorial(5))

        