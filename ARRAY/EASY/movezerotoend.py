def movezerotoend(num):
    count=0
    for i in range(0,len(num)):
        if(num[i]==0):
            count+=1
        else:
            num[i-count]=num[i]

    n=len(num)
    for i in range(0,count):
        num[n-count+i]=0


    return num

print(movezerotoend([1,0,2,3,0,0,4,5,1]))
