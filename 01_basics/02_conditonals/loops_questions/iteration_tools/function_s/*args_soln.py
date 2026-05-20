# write a function take take many number of argumnents and return their value in sum :
def sum_all(*args):
    print(args) #sirf args print karne se value touple me aati hai aur touble iterabe hai iterate karkw hm aur bhi changing kar sakte hai
    #print(*args)
    for i in args:
        print(i*3)
    return sum(args) #sum is the defaukt method i python i n which you can give many values:

print(sum_all(1,2,3,4))
# print(sum_all(1,2,3,4.23))
# print(sum_all(1,2,3,4,12))
    