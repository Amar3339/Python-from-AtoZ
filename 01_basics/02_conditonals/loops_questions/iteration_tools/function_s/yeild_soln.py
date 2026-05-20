# write a genrator function that yield  even number upto specefic limit
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
        
for num in even_generator(100):
    print(num)
for a in even_generator(50):
    print(a)    
        
    
