def isarmstrong(num):
    if(num<=1):
        return True
    dup=num
    newnum=0
    while(num>0):
        temp=num%10
        newnum+=temp*temp*temp
        num=num//10
    return newnum==dup
#371
print(isarmstrong(1634))