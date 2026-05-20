# age group categorization
# classify a person's age grpup:Child(<13),Teenageer(13-19),Adult(20-59),Senior(60+).

# age=int(input("enter your age"))

# if age<13:
#     print("Child")
# elif age<20:
#     print("Teenager")
# elif age<60:
#     print("Adult")
# else:
#     print("Seniior")         
# 900=009
num=900
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)   