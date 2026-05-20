# print **kwargs fumctons
# means= create a functions that accept any number of arguments and print them in the format of  key  value pairs:


# create a functions that accept any number of arguments and print them in the format of  key  value pairs:

def  print_kwargs(**kwargs):
    for key, Value in kwargs.items(): #kwargs ke item pe hm loop laga rhe hai isliye .items ka use huahai.
        print(f"{key}:{Value}")
        
print_kwargs(name="amar", power="lazer" )        
print_kwargs(name="amar", power="lazer" )        
print_kwargs(name="amar", power="lazer" ,bhakt="mahakal",kind="honesty")        