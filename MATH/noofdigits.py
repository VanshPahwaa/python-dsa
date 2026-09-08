import math
def noofdigits(num):
    count=0
    while(num>0):
        num=num//10
        count+=1
    return count

def noofdigits(num):
    count=math.ceil(math.log10(num))
    return count

def noofdigitsrecursive(num):
    if(num<=0):
        return 0
    return 1 + noofdigitsrecursive(num//10)


print(noofdigits(56789))
print(noofdigitsrecursive(56789))